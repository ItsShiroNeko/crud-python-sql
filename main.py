import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="db_mahasiswa"
)

cursor = db.cursor()

def create(nama, umur, jurusan):
    sql = "INSERT INTO mahasiswa (nama, umur, jurusan) VALUES (%s, %s, %s)"
    values = (nama, umur, jurusan)
    cursor.execute(sql, values)
    db.commit()

def read():
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def update(id, nama, umur, jurusan):
    sql = "UPDATE mahasiswa SET nama = %s, umur = %s, jurusan = %s WHERE id = %s"
    values = (nama, umur, jurusan, id)
    cursor.execute(sql, values)
    db.commit()

def delete(id):
    sql = "DELETE FROM mahasiswa WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    db.commit()