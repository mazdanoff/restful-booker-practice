PROPER = {
    "firstname": "Romuald",
    "lastname": "Mean",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2020-03-12",
        "checkout": "2020-03-25"
    },
    "additionalneeds": "Yellow rubber duck"
}

EMPTY_FIRSTNAME = {
    "firstname": "",
    "lastname": "",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2020-03-12",
        "checkout": "2020-03-25"
    },
    "additionalneeds": "Yellow rubber duck"
}

WRONG_VALUE_TYPE = {
    "firstname": "Romuald",
    "lastname": "Mean",
    "totalprice": "$111",
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2020-03-12",
        "checkout": "2020-03-25"
    },
    "additionalneeds": "Yellow rubber duck"
}

CHECKIN_AFTER_CHECKOUT = {
    "firstname": "Romuald",
    "lastname": "Mean",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2022-03-12",
        "checkout": "2020-03-25"
    },
    "additionalneeds": "Yellow rubber duck"
}
