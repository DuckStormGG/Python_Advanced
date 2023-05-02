SELECT DISTINCT full_name
FROM students s
         JOIN students_groups sg on s.group_id = sg.group_id
         JOIN assignments a on a.teacher_id = sg.teacher_id
         JOIN assignments_grades g on a.assisgnment_id = g.assisgnment_id
WHERE g.assisgnment_id =
      (SELECT assisgnment_id
       FROM assignments_grades
       GROUP BY assisgnment_id
       ORDER BY AVG(grade) DESC
       LIMIT 1)
