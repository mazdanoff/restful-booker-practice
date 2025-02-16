import pytest
from hamcrest import assert_that, equal_to
from requests import post

from conf.paths import test_data_json, test_data_xml, test_data_url
from endpoints import CREATE_BOOKING_URL
from tests.create_booking.test_data import EMPTY_FIRSTNAME, PROPER, WRONG_VALUE_TYPE, CHECKIN_AFTER_CHECKOUT

test_files = {
    "application/json": test_data_json,
    "text/xml": test_data_xml,
    "application/x-www-form-urlencoded": test_data_url,
}

content_types = [
    "application/json",
    "text/xml",
    "application/x-www-form-urlencoded",
]

accepts = [
    "application/json",
    "application/xml",
]

def test_create_booking_status_code():
    response = post(CREATE_BOOKING_URL, data=PROPER)
    assert_that(response.status_code, equal_to(200),
                f"Received {response.status_code} instead of 200")

# def test_create_booking_firstname_lastname():
#     response = post(CREATE_BOOKING_URL, data=PROPER)
#     assert_that(response.status_code, equal_to(200),
#                 f"Received {response.status_code} instead of 200")

@pytest.mark.parametrize("content_type", content_types)
@pytest.mark.parametrize("accept", accepts)
def test_create_booking_contenttype_accept(content_type, accept):
    headers = {'Content-Type': content_type, 'Accept': accept}
    data = open(test_files[content_type], 'rb')

    response = post(CREATE_BOOKING_URL, data=data, headers=headers)
    assert_that(response.status_code, equal_to(200),
                f"Received {response.status_code} instead of 200")

def test_create_booking_empty_name_request():
    response = post(CREATE_BOOKING_URL, json=EMPTY_FIRSTNAME)
    assert_that(response.status_code, equal_to(400),
                f"Received {response.status_code} instead of 400")
    # Service takes in empty values for names
    # incognito mode!

def test_create_booking_wrong_value_type_request():
    headers = {'Content-Type': "application/json", 'Accept': "application/json"}

    response = post(CREATE_BOOKING_URL, json=WRONG_VALUE_TYPE, headers=headers)
    assert_that(response.status_code, equal_to(400),
                f"Received {response.status_code} instead of 400")
    # sent totalprice value as a string, a null was returned in its place
    # free booking!

def test_create_booking_checkin_after_checkout_request():
    headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    response = post(CREATE_BOOKING_URL, json=CHECKIN_AFTER_CHECKOUT, headers=headers)
    assert_that(response.status_code, equal_to(400),
                f"Received {response.status_code} instead of 400")
    # I can do a checkin in 2022 and do a checkout in 2020
    # time travel!
