import json

import pytest
from hamcrest import assert_that, equal_to, is_not
from requests import post

from content_dataclasses.create_booking_request import CreateBookingRequest
from content_dataclasses.create_booking_response import CreateBookingResponse
from endpoints import CREATE_BOOKING_URL
from tests.create_booking.test_data import EMPTY_NAME, PROPER, WRONG_VALUE_TYPE, CHECKIN_AFTER_CHECKOUT

test_data = {
    "application/json": CreateBookingRequest.from_dict(PROPER).to_json(),
    "text/xml": CreateBookingRequest.from_dict(PROPER).to_xml(),
    "application/x-www-form-urlencoded": CreateBookingRequest.from_dict(PROPER).to_url(),
}

def test_create_booking_status_code():
    """Sanity test to check the CreateBooking endpoint. Sends a proper request and expects 200."""
    # NOTE: Documentation says application/json is default.
    # I assume this means headers are optional and will be handled by the API.
    response = post(CREATE_BOOKING_URL, data=test_data["application/json"])  # no headers, responds with 500
    assert_that(response.status_code, equal_to(200),
                f"Received {response.status_code} instead of 200")

@pytest.mark.parametrize("content_type",
            ["application/json", "text/xml", "application/x-www-form-urlencoded"])
@pytest.mark.parametrize("accept",
            ["application/json", "application/xml"])
def test_create_booking_contenttype_accept(content_type, accept):
    """
    Parametrized test that exhausts all combinations of known content types that the API can handle.
    Tested features:
    - API handling of different content types the client declared they sent (Content-Type header)
    - API handling of different content types the client defined they want to receive (Accept header)
    """
    # CANDIDATE NOTE
    #     API documentation says content type can be application/json or text/xml,
    #     but I figured application/x-www-form-urlencoded works just as well
    # NOTE
    #     accept: application/xml tests will fail, as service declares it's responding with text/html,
    #     although the response content seems to be xml-parsable <- ! which should be tested separately !
    headers = {'Content-Type': content_type, 'Accept': accept}
    data = test_data[content_type]

    response = post(CREATE_BOOKING_URL, data=data, headers=headers)
    assert_that(accept in response.headers['Content-Type'],
                f"Expected '{accept}', but received '{response.headers['Content-Type']}'")

def test_create_booking_empty_name_request():
    """
    First name and last name values passed here are simply empty strings.
    While their type is correct, the values are not necessarily (unless the booking service allows anonymous booking...)
    """
    response = post(CREATE_BOOKING_URL, json=EMPTY_NAME)
    assert_that(response.status_code, equal_to(400),
                f"Received {response.status_code} instead of 400")

def test_create_booking_wrong_value_type_request():
    """
    We check/verify how API handles mismatched value types in request body.
    The totalprice value should be an int, but we are passing it on as a string.
    A '$111' instead of 111 is a reasonable mistake one can make.
    """
    response = post(CREATE_BOOKING_URL, json=WRONG_VALUE_TYPE)
    assert_that(response.status_code, equal_to(400),
                f"Received {response.status_code} instead of 400")
    # sent totalprice value as a string, a null was returned in its place
    # free booking, whoo!

def test_create_booking_checkin_after_checkout_request():
    """
    Check-in and check-out dates are formatted correctly, but it doesn't make sense
    for check-in to happen AFTER we declare checking out within the same booking reservation.
    It's a logical error and should also be verified if API can handle this.
    """
    response = post(CREATE_BOOKING_URL, json=CHECKIN_AFTER_CHECKOUT)
    assert_that(response.status_code, equal_to(400),
                f"Received {response.status_code} instead of 400")
    # I can do a checkin in 2022 and do a checkout in 2020
    # time travel!

def test_create_booking_subsequent_requests_have_different_ids():
    """
    Kind of a sanity test that checks if booking IDs are different for different requests.
    """
    response1 = post(CREATE_BOOKING_URL, json=PROPER)
    response1 = CreateBookingResponse.from_dict(json.loads(response1.text))
    response2 = post(CREATE_BOOKING_URL, json=PROPER)
    response2 = CreateBookingResponse.from_dict(json.loads(response2.text))
    assert_that(response1.bookingid, is_not(equal_to(response2.bookingid)),
                "IDs from two different responses are the same")
