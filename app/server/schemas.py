
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class CustomerBase(BaseModel):
    customerid: str
    country: str

class CustomerCreate(CustomerBase):
    pass
    #password: str

class Customer(CustomerBase):
    pass

    class Config:
        orm_mode = True



class ProductBase(BaseModel):
    stockcode: str
    description: Optional[str]
    unitprice: Optional[float]

class ProductCreate(ProductBase):
    pass
    #password: str

class Product(ProductBase):
    pass

    class Config:
        orm_mode = True



class InvoiceBase(BaseModel):
    invoicenumber: str
    invoicedate: datetime
    customerid: str

class InvoiceCreate(InvoiceBase):
    pass
    #password: str

class Invoice(InvoiceBase):
    pass

    class Config:
        orm_mode = True



class InvoiceLineItemBase(BaseModel):
    invoicelineitemid: int
    invoicenumber: str
    stockcode: str
    quantity: int

class InvoiceLineItemCreate(InvoiceLineItemBase):
    pass
    #password: str

class InvoiceLineItem(InvoiceLineItemBase):
    pass

    class Config:
        orm_mode = True


