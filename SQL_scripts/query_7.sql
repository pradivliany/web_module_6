-- Знайти оцінки студентів у окремій групі з певного предмета.

select g.grade, s.group_id, g.subject_id
from grades g left join students s on g.student_id = s.id
where s.group_id = 1 and g.subject_id = 1;
