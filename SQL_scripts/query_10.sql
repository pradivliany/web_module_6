-- Список курсів, які певному студенту читає певний викладач.

select distinct s2.subject_name  from grades g
left join students s on g.student_id = s.id
left join subjects s2 on g.subject_id = s2.id
where g.student_id = 1 and s2.teacher_id = 1;
