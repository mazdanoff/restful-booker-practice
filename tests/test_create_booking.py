import os
from dataclasses import dataclass
from datetime import datetime

import pytest
from hamcrest import assert_that, equal_to
from requests import post

URL = "https://restful-booker.herokuapp.com/booking"
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
tests_path = os.path.join(project_path, "tests")
test_data_path = os.path.join(tests_path, "test_data")
test_data_json = os.path.join(test_data_path, "create_booking.json")
test_data_xml = os.path.join(test_data_path, "create_booking.xml")
test_data_url = os.path.join(test_data_path, "create_booking.txt")

@dataclass
class BookingData:
    bookingid: int
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    checkin: datetime
    checkout: datetime
    additionalneeds: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            bookingid=data["bookingid"],
            firstname=data["booking"]["firstname"],
            lastname=data["booking"]["lastname"],
            totalprice=data["booking"]["totalprice"],
            depositpaid=data["booking"]["depositpaid"],
            checkin=datetime.strptime(data["booking"]["checkin"], "%Y-%M-%D"),
            checkout=datetime.strptime(data["booking"]["checkout"], "%Y-%M-%D"),
            additionalneeds=data["booking"]["additionalneeds"],
        )

params = [
    ("application/json", test_data_json),
    ("application/xml", test_data_xml),
    ("application/x-www-form-urlencoded", test_data_url),
]

@pytest.mark.parametrize("content_type, testdata", params)
def test_create_booking(content_type, testdata):
    headers = {'Content-Type': 'application/json'}
    data = open(test_data_json, 'rb')
    response = post(URL, data=data, headers=headers)
    assert_that(response.status_code, equal_to(200), f"Received {response.status_code} instead of 200")
