create table groups (
	id integer primary key autoincrement,
	group_name varchar(30)
);

create table students (
	id integer primary key autoincrement,
	student_name varchar(30),
	group_id integer not null,
	foreign key (group_id) references groups (id)
);

create table teachers (
	id integer primary key autoincrement,
	teacher_name varchar(30)
);

create table subjects (
	id integer primary key autoincrement,
	subject_name varchar(30),
	teacher_id integer not null,
	foreign key (teacher_id) references teachers (id)
);


create table grades (
	id integer primary key autoincrement,
	grade integer,
	student_id integer not null,
	subject_id integer not null,
	date_of date not null,
	foreign key (student_id) references students (id),
	foreign key (subject_id) references subjects (id)
);
