SELECT t.full_name, AVG(grade) as avg
FROM assignments
JOIN assignments_grades ag on assignments.assisgnment_id = ag.assisgnment_id
JOIN teachers t on t.teacher_id = assignments.teacher_id
GROUP BY t.teacher_id
ORDER BY avg
LIMIT 1

