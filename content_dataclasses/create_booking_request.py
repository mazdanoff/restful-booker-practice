import json
from dataclasses import dataclass

from dict2xml import dict2xml

from helpers.data_to_url import data_to_url


@dataclass
class CreateBookingRequest:
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    checkin: str
    checkout: str
    additionalneeds: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            firstname=data["firstname"],
            lastname=data["lastname"],
            totalprice=data["totalprice"],
            depositpaid=data["depositpaid"],
            checkin=data["bookingdates"]["checkin"],
            checkout=data["bookingdates"]["checkout"],
            additionalneeds=data["additionalneeds"],
        )

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": {
                "checkin": self.checkin,
                "checkout": self.checkout,
            },
            "additionalneeds": self.additionalneeds,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_xml(self):
        data = dict(booking=self.to_dict())
        return dict2xml(data)

    def to_url(self):
        return data_to_url(self.to_dict())
