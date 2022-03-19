
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class CustomerBase(BaseModel):
    CustomerID: str
    Country: str

class CustomerCreate(CustomerBase):
    password: str

class Customer(CustomerBase):
    pass

    class Config:
        orm_mode = True



class ProductBase(BaseModel):
    StockCode: str
    Description: str
    UnitPrice: float

class ProductCreate(ProductBase):
    pass
    #password: str

class Product(ProductBase):
    pass

    class Config:
        orm_mode = True



class InvoiceBase(BaseModel):
    InvoiceNumber: str
    InvoiceDate: datetime
    CustomerID: str

class InvoiceCreate(InvoiceBase):
    pass
    #password: str

class Invoice(InvoiceBase):
    pass

    class Config:
        orm_mode = True



class InvoiceLineItemBase(BaseModel)
    InvoiceLineItemID: int
    InvoiceNumber: str
    StockCode: str
    Quantity: int

class InvoiceLineItemCreate(InvoiceLineItemBase):
    pass
    #password: str

class InvoiceLineItem(InvoiceLineItemBase):
    pass

    class Config:
        orm_mode = True


