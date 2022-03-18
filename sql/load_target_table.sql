


INSERT INTO ecomm_prod (
InvoiceNo,
StockCode,
Description,
Quantity,
InvoiceDate,
UnitPrice,
CustomerID,
Country
)
SELECT
	InvoiceNo,
	StockCode,
	Description,
	CAST(Quantity AS INTEGER) AS Quantity,
	CAST(InvoiceDate AS DATE) AS InvoiceDate,
	CAST(UnitPrice AS DECIMAL(10,4)) AS UnitPrice,
	CustomerID,
	Country
FROM ecomm_raw;
