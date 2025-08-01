import sqlite3
import os


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db") # conn: connection
    cursor = conn.cursor() #db'de dolaşır
    return conn, cursor

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY,
            name VARCHAR NOT NULL,
            age INT,
            email VARCHAR UNIQUE,
            city VARCHAR
            )
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INT
            )
    ''')

def insert_sample_data(cursor):
    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)",students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)",courses)
    print("Sample data inserted successfully")


# reading operations
def basic_sql_operations(cursor):
    # SELECT ALL
    print("----------SELECT ALL -------------")
    cursor.execute("SELECT * FROM Students ")
    records = cursor.fetchall() #fetch data
    for row in records:
        #print(row)
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")

    # SELECT Columns
    print("----------SELECT Columns -------------")
    cursor.execute("SELECT name,age FROM Students")
    records = cursor.fetchall() #fetch data
    for row in records:
        print(row)

    # WHERE clause
    print("----------WHERE clause-------------")
    cursor.execute("SELECT * FROM Students WHERE age=20")
    records = cursor.fetchall() #fetch data
    for row in records:
        print(row)

    # WHERE clause
    print("----------WHERE clause 2-------------")
    cursor.execute("SELECT * FROM Students WHERE city = 'Boston'")
    records = cursor.fetchall() #fetch data
    for row in records:
        print(row)

    # ORDER BY
    print("----------ORDER BY-------------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall() #fetch data
    for row in records:
        print(row)

    # LIMIT
    print("----------LIMIT-------------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall() #fetch data
    for row in records:
        print(row)


# basic operations
def sql_update_insert_delete_operations(cursor,conn):
    # insert
    cursor.execute("INSERT INTO Students VALUES (6,'Frank miller', 23, 'frankmiller@gmail.com', 'French')")
    conn.commit() # print permanently

    # update
    cursor.execute("UPDATE Students SET age=26 WHERE id=6")
    conn.commit()

    # delete
    cursor.execute("DELETE FROM Students WHERE id=6")
    conn.commit()


def aggregate_function(cursor):
    # count
    print("---------Aggregate function count-------------")
    cursor.execute("SELECT COUNT(*) FROM Students") # num of samples in the table
    #result = cursor.fetchall() # [(5,)] list+tuple
    result = cursor.fetchone()  # tuple (just for one result)
    print(result)    # (5,)
    print(result[0]) # 5

    # average
    print("---------Aggregate function average-------------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # max
    print("---------Aggregate function max-min-------------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # group by
    print("---------Aggregate function group by-------------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)


def operations(cursor):
    print("--------information of all courses")
    cursor.execute("SELECT * FROM Courses")
    print(cursor.fetchall())

    print("----------instructor name & course name-----------")
    cursor.execute("SELECT course_name,instructor FROM Courses")
    print(cursor.fetchall())

    print("-----------only students aged 21-------------")
    cursor.execute("SELECT * FROM Students WHERE age=21")
    print(cursor.fetchall())

    print("-------------students living in Chicago only---------------")
    cursor.execute("SELECT * FROM Students WHERE city='Boston' ")
    print(cursor.fetchall())

    print("-------------courses given by Dr. Anderson---------------")
    cursor.execute("SELECT * FROM Courses WHERE instructor='Dr. Anderson' ")
    print(cursor.fetchall())

    print("-------------students name starting with A ---------------")
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'A%' ")
    print(cursor.fetchall())

    print("-------------courses credit>3 ---------------")
    cursor.execute("SELECT * FROM Courses WHERE credits>=3 ")
    print(cursor.fetchall())

    print("-------------Alphabetical names of students---------------")
    cursor.execute("SELECT * FROM Students ORDER BY name ")
    print(cursor.fetchall())

    print("-------------Alphabetical names of students & age>20---------------")
    cursor.execute("SELECT name,age FROM Students WHERE age>20 ORDER BY name ")
    print(cursor.fetchall())

    print("-------------students living in Chicago or new york---------------")
    cursor.execute("SELECT name,city FROM Students WHERE city IN ('Chicago', 'New York') ")
    print(cursor.fetchall())

    print("-------------students not living in new york---------------")
    cursor.execute("SELECT name,city FROM Students WHERE city != 'New York' ")
    print(cursor.fetchall())

    print("-------------students not living in new york---------------")
    cursor.execute("SELECT name,city FROM Students WHERE city NOT IN ('New York','Chicago') ")
    print(cursor.fetchall())



def main():
    conn, cursor = create_database()

    try:
        create_table(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_insert_delete_operations(cursor,conn)
        aggregate_function(cursor)
        operations(cursor)
        conn.commit() # Değişiklikleri kaydet

    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()
        print("db connection closed")


if __name__ == "__main__":
    main()



'''
Nesne (Object): cursor sizin nesnenizdir. Veritabanıyla etkileşim kuran bir varlık gibi düşünebilirsiniz.
Metot (Method): execute(), fetchall(), fetchone() gibi fonksiyonlar bu nesnenin yapabildiği eylemlerdir, yani onun metotlarıdır.
Bir metoda, ait olduğu nesneyi tekrar parametre olarak vermenize gerek yoktur.

Basit bir benzetme yapalım: 🚗
Bir arabanız (nesne) var ve hızlan() adında bir metodu (eylemi) var. Arabayı hızlandırmak için araba.hızlan() dersiniz. 
hızlan(araba) demezsiniz, çünkü hızlan eylemi zaten o arabaya aittir.

records = cursor.fetchall(): Aynı cursor nesnesine "içinde tuttuğun bütün sonuçları bana ver" komutunu verirsiniz. 
fetchall() metodu, ait olduğu cursor'ın son çalıştırdığı sorgunun sonuçlarını otomatik olarak getirir.
'''