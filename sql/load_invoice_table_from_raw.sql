
INSERT INTO Invoice (
	InvoiceNumber,
	InvoiceDate,
	CustomerID
)
SELECT DISTINCT
	e1.InvoiceNo AS InvoiceNumber,
	TO_TIMESTAMP(e1.InvoiceDate, 'MM/DD/YYYY HH24:MI') AS InvoiceDate,
	e1.CustomerID
FROM ecomm_raw e1
JOIN Customer c1
ON (c1.CustomerID = e1.CustomerID)
WHERE e1.InvoiceNo IS NOT NULL
ON CONFLICT DO NOTHING;
