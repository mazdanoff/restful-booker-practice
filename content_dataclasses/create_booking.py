from dataclasses import dataclass
from datetime import datetime


@dataclass
class CreateBookingResponse:
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
