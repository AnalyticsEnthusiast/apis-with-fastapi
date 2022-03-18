
INSERT INTO Product (
	StockCode,
	Description,
	UnitPrice
)
SELECT DISTINCT
	StockCode,
	Description,
	CAST(UnitPrice AS DECIMAL(12,4)) AS UnitPrice
	FROM ecomm_raw
WHERE StockCode IS NOT NULL
ON CONFLICT DO NOTHING;
