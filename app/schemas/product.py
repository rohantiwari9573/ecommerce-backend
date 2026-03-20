from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True