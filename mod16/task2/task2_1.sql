SELECT c.full_name, m.full_name, o.purchase_amount, o.date
FROM "order" o
         INNER JOIN customer c on c.customer_id = o.customer_id
         INNER JOIN manager m on m.manager_id = o.manager_id