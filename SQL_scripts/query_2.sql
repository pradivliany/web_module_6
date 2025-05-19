-- Знайти студента із найвищим середнім балом з певного предмета.


select round(avg(g.grade), 2) as average_grade, s.id as student_id
from grades g left join students s on g.student_id = s.id
where subject_id = 1
group by s.id
order by average_grade desc
limit 1
;
