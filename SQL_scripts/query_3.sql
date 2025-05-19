-- Знайти середній бал у групах з певного предмета.

select round(avg(grades.grade), 2) as average_grade, students.group_id
from grades left join students on student_id = students.id
where grades.subject_id = 1
group by students.group_id;