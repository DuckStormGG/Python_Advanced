SELECT s.group_id                                                          AS id,
       COUNT(DISTINCT s.student_id)                                        AS students,
       AVG(g.grade)                                                        AS avg,
       COUNT(DISTINCT CASE WHEN g.grade IS NULL THEN s.student_id END)     AS work_not_submitted,
       COUNT(DISTINCT CASE WHEN g.date > a.due_date THEN s.student_id END) AS overdue,
       COUNT(DISTINCT g.grade_id)                                          AS attempts
FROM students s
         LEFT JOIN assignments_grades g ON s.student_id = g.student_id
         LEFT JOIN assignments a ON g.assisgnment_id = a.assisgnment_id
GROUP BY id;