SELECT c1.full_name, c2.full_name
FROM customer as c1
         INNER JOIN customer as c2
                    ON c1.city = c2.city
                        AND c1.manager_id = c2.manager_id
                        AND c1.full_name != c2.full_name