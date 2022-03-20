import uvicorn

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.server import crud, models, schemas
from app.server.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    response = RedirectResponse(url='/docs')
    return response


# Add a new Customer
#@app.post("/customer")
#def create_customer(item: Customer): #body awaits a json with customer information
# This is how to work with and return a item
#   country = item.country
#   return {item.country}
#
#   # You would add here the code for creating a Customer in the database
#
#    # Encode the created customer item if successful into a JSON and return it to the client with 201
#    json_compatible_item_data = jsonable_encoder(item)
#    return JSONResponse(content=json_compatible_item_data, status_code=201)


# Get a customer by customer id
@app.get("/customer/{customer_id}", response_model=schemas.Customer) 
def read_customer(customer_id: str, db: Session = Depends(get_db)):
    db_customer=crud.get_customer(db, cust_id=customer_id)

    if db_customer is None:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="Customer not found")
    else:
        return db_customer

# Create a new invoice for a customer
#@app.post("/customer/{customer_id}/invoice")
#def create_invoice(customer_id: str, invoice: Invoice):
#    
#    # Add the customer link to the invoice
#    invoice.customer.url = "/customer/" + customer_id
#    
#    # Turn the invoice instance into a JSON string and store it
#    jsonInvoice = jsonable_encoder(invoice)
#    fakeInvoiceTable[invoice.invoice_no] = jsonInvoice
#
#    # Read it from the store and return the stored item
#    ex_invoice = fakeInvoiceTable[invoice.invoice_no]
#    
#    return JSONResponse(content=ex_invoice) 

# Return all invoices for a customer
@app.get("/customer/{customer_id}/invoice", response_model=List[schemas.Invoice])
def get_invoices(customer_id: str, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice_by_cust_id(db, cust_id=customer_id)

    if db_invoice is None:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="No invoice found")
    else:
        return db_invoice


# Return a specific invoice
@app.get("/invoice/{invoice_no}", response_model=schemas.Invoice)
def get_invoice(invoice_no: str, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice(db, inv_id=invoice_no)
    
    if db_invoice is None:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="No invoice found")
    else:
        return db_invoice


# Get Product based on stock code
@app.get("/product/{stock_code}", response_model=schemas.Product)
def get_product(stock_code: str, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, prod_id=stock_code)

    if db_product is None:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="No product found")
    else:
        return db_product

# Get Line Items on an Invoice
@app.get("/invoicelineitem/{invoice_no}", response_model=List[schemas.InvoiceLineItem])
def get_invoice_line_item(invoice_no: str, db: Session = Depends(get_db)):
    db_line_items = crud.get_invoice_line_items(db, invoice_no=invoice_no)

    if db_line_items is None:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="No line items found for that invoice number")
    else:
        return db_line_items

