SELECT c.full_name
FROM customer c
WHERE c.customer_id NOT IN (
    SELECT "order".customer_id
    FROM "order"
    )