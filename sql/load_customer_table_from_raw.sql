
INSERT INTO customer (
	CustomerID, 
	Country
)
SELECT DISTINCT
	CustomerID,
	Country
FROM ecomm_raw
WHERE CustomerID IS NOT NULL
ON CONFLICT DO NOTHING;
