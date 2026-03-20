from pydantic import BaseModel


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float

    class Config:
        from_attributes = True