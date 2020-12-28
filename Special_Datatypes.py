import uvicorn
from fastapi import FastAPI
from pydantic.types import PaymentCardBrand, PaymentCardNumber, constr
from pdantic.color import Color
from datetime import datetime, time, timedelta

app = FastAPI()

@app.post("/items")
async def update_item(*,
                      start_datetime: datetime = Body(None),
                      end_datetime: datetime = Body(None),
                      repeat_at: time = Body(None),
                      process_after: timedelta = Body(None),):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
        "process_after": process_after.seconds
    }


@app.post("/items")
async def update_item(*, setColor: Color,):
    return {
        "Item color": setColor,
        "Name": setColor.as_named(),
        "Hex": setColor.as_hex(),
        "RGB": setColor.as_rgb_tuple()
    }


@app.post("/items")
async def update_item(*, cardNumber: PaymentCardNumber, cardBrand: PaymentCardBrand):
    return {
        "Card Number": cardNumber,
        "Brand": cardBrand
    }


class Card(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    number: PaymentCardNumber
    exp: datetime

    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < datetime.today()


@app.post("/pay")
async def update_payType(*, card: Card):
    return {
        "Brand": card.number.brand ,
        "Bin": card.number.bin,
        "Last4 Digits": card.number.last4,
        "Masked Num": card.number.masked
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
