from hamcrest import assert_that, equal_to
from requests import get

URL = "https://restful-booker.herokuapp.com/ping"

def test_sanity():
    response = get(URL)
    assert_that(response.status_code, equal_to(201), f"Received {response.status_code} instead of 201")
    assert_that(response.headers['Content-Type'], equal_to('text/plain; charset=utf-8'), f"Content type differs: {response.headers['Content-Type']}")
    assert_that(response.text, equal_to("Created"), f"Received a different response text: {response.text}")
