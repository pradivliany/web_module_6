-- Знайти список курсів, які відвідує студент.

select distinct g.subject_id as unique_subjects_id
from grades g left join students s on g.student_id = s.id
where g.student_id = 1;
