SELECT o.order_no, m.full_name, c.full_name
FROM "order" o
         INNER JOIN manager m
                    ON o.manager_id = m.manager_id
         INNER JOIN customer c
                    ON o.customer_id = c.customer_id
WHERE m.city != c.city