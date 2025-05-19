-- Знайти які курси читає певний викладач.

select teachers.teacher_name, subjects.subject_name
from teachers left join subjects on teachers.id = subjects.teacher_id
where subjects.teacher_id = 1;
