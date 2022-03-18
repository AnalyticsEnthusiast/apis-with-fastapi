
INSERT INTO InvoiceLineItem (
	InvoiceNumber,
	StockCode,
	Quantity
)
SELECT DISTINCT
	e1.InvoiceNo AS InvoiceNumber,
	e1.StockCode,
	CAST(e1.Quantity AS INTEGER) AS Quantity
FROM ecomm_raw e1
JOIN Product p1
ON (p1.StockCode = e1.StockCode)
JOIN Invoice i1
ON (i1.InvoiceNumber = e1.InvoiceNo)
ON CONFLICT DO NOTHING;

