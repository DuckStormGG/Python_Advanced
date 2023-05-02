SELECT full_name, AVG(grade) as avg
FROM students s
JOIN assignments_grades g on s.student_id = g.student_id
GROUP BY s.student_id
ORDER BY avg DESC
LIMIT 10