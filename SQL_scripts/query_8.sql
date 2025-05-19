-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

select round(avg(g.grade), 2) as average_grade
from grades g left join subjects s on g.subject_id = s.id
where s.teacher_id = 1;
