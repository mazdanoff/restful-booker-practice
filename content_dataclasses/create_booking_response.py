from dataclasses import dataclass


@dataclass
class CreateBookingResponse:
    bookingid: int
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
            bookingid=data["bookingid"],
            firstname=data["booking"]["firstname"],
            lastname=data["booking"]["lastname"],
            totalprice=data["booking"]["totalprice"],
            depositpaid=data["booking"]["depositpaid"],
            checkin=data["booking"]["bookingdates"]["checkin"],
            checkout=data["booking"]["bookingdates"]["checkout"],
            additionalneeds=data["booking"]["additionalneeds"],
        )
