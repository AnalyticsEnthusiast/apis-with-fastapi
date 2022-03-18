
COPY ecomm_raw(InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) 
FROM '/home/dfoley/Documents/DataEngineeringCourse/apis-with-fastapi/data/data_clean.csv'
DELIMITER ','
CSV HEADER;
