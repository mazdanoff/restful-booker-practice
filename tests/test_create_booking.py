import json
import os
from dataclasses import dataclass
from datetime import datetime

from hamcrest import assert_that, equal_to
from requests import post

URL = "https://restful-booker.herokuapp.com/booking"
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
tests_path = os.path.join(project_path, "tests")
test_data_path = os.path.join(tests_path, "test_data")
test_data_file = os.path.join(test_data_path, "create_booking.json")

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

def test_create_booking():
    headers = {'Content-Type': 'application/json'}
    data = open(test_data_file, 'rb')
    response = post(URL, data=data, headers=headers)
    assert_that(response.status_code, equal_to(200), f"Received {response.status_code} instead of 200")
