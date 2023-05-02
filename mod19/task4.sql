SELECT id, AVG(count) AS avg, MAX(count) AS max, MIN(count) AS min
FROM (SELECT a.group_id               as id,
             SUM(g.date > a.due_date) as count
      FROM assignments a
               INNER JOIN assignments_grades g
                          ON a.assisgnment_id = g.assisgnment_id
      GROUP BY id, a.assisgnment_id)
GROUP BY id