-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

select round(avg(g.grade), 2) as average_grade, s.id as student_id
from grades g left join students s on g.student_id = s.id
group by s.id
order by average_grade desc
limit 5
;
