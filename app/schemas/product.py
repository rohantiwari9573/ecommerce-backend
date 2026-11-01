from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    price: float = Field(gt=0)


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True