SELECT AVG(grade) as avg
FROM assignments_grades g
         JOIN assignments a ON g.assisgnment_id = a.assisgnment_id
WHERE assignment_text LIKE '%прочитать%'
   OR '%выучить%'