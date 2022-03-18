
DROP TABLE IF EXISTS InvoiceLineItem;
DROP TABLE IF EXISTS Invoice;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Product;

-- Customer Table
CREATE TABLE IF NOT EXISTS Customer (
	CustomerID VARCHAR(100) NOT NULL,
	Country VARCHAR(100),
	PRIMARY KEY(CustomerID)
);

-- Product Table
CREATE TABLE IF NOT EXISTS Product (
	StockCode VARCHAR(100) NOT NULL,
	Description VARCHAR(255),
	UnitPrice DECIMAL(12,4),
	PRIMARY KEY(StockCode)
);

-- Invoice Table
CREATE TABLE IF NOT EXISTS Invoice (
	InvoiceNumber VARCHAR(100) NOT NULL,
	InvoiceDate TIMESTAMP,
	CustomerID VARCHAR(100),
	PRIMARY KEY(InvoiceNumber),
	CONSTRAINT fk_customer FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID)
);

-- Invoice Line Item Table
CREATE TABLE IF NOT EXISTS InvoiceLineItem (
	InvoiceLineItemID SERIAL PRIMARY KEY NOT NULL,
	InvoiceNumber VARCHAR(100),
	StockCode VARCHAR(100),
	Quantity INTEGER,
	CONSTRAINT fk_product FOREIGN KEY(StockCode) REFERENCES Product(StockCode),
	CONSTRAINT fk_invoice FOREIGN KEY(InvoiceNumber) REFERENCES Invoice(InvoiceNumber)
);

