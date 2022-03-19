
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base


class Customer(Base):
    __tablename__ = "customer"

    CustomerID = Column(String, primary_key=True)
    Country = Column(String)
    
    invoices = relationship("Invoice", back_populates="customers")


class Product(Base):
    __tablename__ = "product"

    StockCode = Column(String, primary_key=True)
    Description = Column(String)
    UnitPrice = Column(Float)


class Invoice(Base):
    __tablename__ = "invoice"

    InvoiceNumber = Column(String, primary_key=True)
    InvoiceDate = Column(DateTime)
    CustomerID = Column(String, ForeignKey("Customer.CustomerID"))

    customers = relationship("Customer", back_populates="invoices")
    invoices = relationship("InvoiceLineItem", back_populates="invoices")


class InvoiceLineItem(Base):
    __tablename__ = "invoicelineitem"

    InvoiceLineItem = Column(Integer, primary_key=True)
    Quantity = Column(Integer)

    StockCode = Column(String, ForeignKey("Product.StockCode"))
    InvoiceNumber = Column(String, ForeignKey("Invoice.InvoiceNumber"))

    invoices = relationship("Invoice", back_populates="invoices")
    
