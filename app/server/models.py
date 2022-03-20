
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base


class Customer(Base):
    __tablename__ = "customer"

    customerid = Column(String, primary_key=True)
    country = Column(String)
    
    #invoices = relationship("Invoice", back_populates="customers")


class Product(Base):
    __tablename__ = "product"

    stockcode = Column(String, primary_key=True)
    description = Column(String)
    unitprice = Column(Float)
    
    #invoicelineitem_rel = relationship("InvoiceLineItem", backref="Product", lazy="dynamics")


class Invoice(Base):
    __tablename__ = "invoice"

    invoicenumber = Column(String, primary_key=True)
    invoicedate = Column(DateTime)
    customerid = Column(String, ForeignKey("Customer.customerid"))

    #customers = relationship("Customer", back_populates="invoices")
    #invoicelineitem_rel = relationship("InvoiceLineItem", backref="Invoice", uselist=False)


class InvoiceLineItem(Base):
    __tablename__ = "invoicelineitem"

    invoicelineitemid = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    stockcode = Column(String, ForeignKey("Product.stockcode"))
    invoicenumber = Column(String, ForeignKey("Invoice.invoicenumber"))
    
    #product_rel = relationship("Product", back_populates="invoicelineitem_rel", uselist=False)
    #invoice_rel = relationship("Invoice", lazy="joined")
    #invoices = relationship("Invoice", back_populates="invoices")
    

