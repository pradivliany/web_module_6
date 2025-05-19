-- Знайти список студентів у певній групі.

select students.student_name as student_name
from students left join groups on students.group_id = groups.id
where groups.id = 1;
