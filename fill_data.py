import random
import sqlite3
import faker
from create_db import DATABASE

COUNT_STUDENTS = 30
COUNT_SUBJECTS = 5
COUNT_GROUPS = 3
COUNT_TEACHERS = 3
COUNT_GRADES_EACH_STUDENT = 15


def generate_fake_data():
    subjects_names = ["Math", "Physics", "World History", "Chemistry", "Programming"]
    groups = [["Group-A"], ["Group-B"], ["Group-C"]]
    teachers = []
    subjects = []
    students = []
    grades = []

    fake_data = faker.Faker()

    for _ in range(COUNT_TEACHERS):
        teachers.append([fake_data.name()])

    for sub in subjects_names:
        subjects.append([sub, random.randint(1, 3)])

    for _ in range(COUNT_STUDENTS):
        student_name = fake_data.name()
        students.append([student_name, random.randint(1, 3)])

    for student_id in range(1, 31):
        for i in range(COUNT_GRADES_EACH_STUDENT):
            random_grade = random.randint(0, 100)
            grades.append(
                [
                    random_grade,
                    student_id,
                    random.randint(1, 5),
                    fake_data.date_this_year(),
                ]
            )

    return groups, teachers, subjects, students, grades


def insert_data(groups, teachers, subjects, students, grades):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        sql_to_groups = "insert into groups (group_name) values (?);"
        sql_to_teachers = "insert into teachers (teacher_name) values (?);"
        sql_to_subjects = (
            "insert into subjects (subject_name, teacher_id) values (?, ?);"
        )
        sql_to_students = "insert into students (student_name, group_id) values (?, ?);"
        sql_to_grades = "insert into grades (grade, student_id, subject_id, date_of) values (?, ?, ?, ?);"

        cursor.executemany(sql_to_groups, groups)
        cursor.executemany(sql_to_teachers, teachers)
        cursor.executemany(sql_to_subjects, subjects)
        cursor.executemany(sql_to_students, students)
        cursor.executemany(sql_to_grades, grades)

        connection.commit()


if __name__ == "__main__":
    fake_groups, fake_teachers, fake_subjects, fake_students, fake_grades = (
        generate_fake_data()
    )
    insert_data(fake_groups, fake_teachers, fake_subjects, fake_students, fake_grades)
