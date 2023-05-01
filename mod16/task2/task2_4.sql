SELECT c.full_name, o.order_no
FROM customer c
         INNER JOIN "order" o
                    ON c.customer_id = o.customer_id
WHERE c.manager_id IS NULL