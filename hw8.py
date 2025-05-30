import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Таблицы пользователей, оценок, хобби, предметов
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS hobbies (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    hobby TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    subject_id INTEGER,
    grade REAL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
)
''')

# Пример данных
cursor.executescript('''
DELETE FROM users;
DELETE FROM hobbies;
DELETE FROM subjects;
DELETE FROM grades;

INSERT INTO users (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO hobbies (user_id, hobby) VALUES
(1, 'Reading'),
(1, 'Swimming'),
(2, 'Chess'),
(3, 'Drawing');

INSERT INTO subjects (id, name) VALUES
(1, 'Math'),
(2, 'Physics'),
(3, 'History');

INSERT INTO grades (user_id, subject_id, grade) VALUES
(1, 1, 5),
(1, 2, 4),
(1, 3, 5),
(2, 1, 3),
(2, 2, 4),
(3, 1, 5),
(3, 3, 5);
''')
conn.commit()
def create_user_hobby_subjects_view():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS user_hobby_subject_count AS
    SELECT u.name AS user_name,
           h.hobby AS hobby,
           COUNT(DISTINCT g.subject_id) AS subjects_count
    FROM users u
    LEFT JOIN hobbies h ON u.id = h.user_id
    LEFT JOIN grades g ON u.id = g.user_id
    GROUP BY u.id, h.hobby
    ''')
    print("Представление user_hobby_subject_count создано!")

create_user_hobby_subjects_view()
def show_user_hobby_subjects_view():
    cursor.execute('SELECT * FROM user_hobby_subject_count')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

show_user_hobby_subjects_view()
