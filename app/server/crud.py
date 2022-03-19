
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import schemas, models
from datetime import datetime
from gen_stock_codes import generate_stock_codes

def get_customer(db: Session, cust_id: str):
    return db.query(models.Customer).filter(models.Customer.CustomerID == cust_id).first() 

def get_product(db: Session, prod_id: str):
    return db.query(models.Product).filter(models.Product.StockCode == prod_id).first()

def get_invoice(db: Session, inv_id: str):
    return db.query(models.Invoice).filter(models.Invoice.InvoiceNumber == inv_id).first()

#def get_invoice_lines(db: Session, inv_id: str):
#    pass
def get_max_custid(db: Session):
    return db.query(func.max(models.Customer.CustomerID)).scalar()

def get_max_invid(db: Session):
    return db.query(func.max(models.Invoice.InvoiceNumber)).scalar()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    max_cust_id = get_max_cust_id(db)
    new_cust_id = max_cust_id + 1

    db_customer = models.Customer(CustomerID=new_cust_id, Email=customer.Email, Country=customer.Country)

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_invoice(db: Session, invoice: schemas.InvoiceCreate, cust_id: str):
    max_inv_id = get_max_invid(db)
    new_inv_id = max_inv_id + 1
    current_datetime = datetime.now() 

    db_invoice = models.Invoice(InvoiceNumber=new_inv_id, InvoiceDate=current_datetime, CustomerID=cust_id)

    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def check_product_exists(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.Description == product_name).first()

def create_product(db: Session, product: schemas.ProductCreate, product_name: str, unit_price: int):
    if not check_product_exists(db, product_name):
        new_stock_code = generate_stock_code()
        db_product = models.Product(StockCode=new_stock_code, Description=product_name, UnitPrice=unit_price)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        return None

