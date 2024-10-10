import mysql.connector

# เชื่อมต่อกับฐานข้อมูล
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="students"
)

# สร้าง cursor สำหรับการดำเนินการ SQL
cursor = mydb.cursor()

# ฟังก์ชันเพิ่มข้อมูลลงในฐานข้อมูล
def insert_student(student_code, name, email, address):
    sql = "INSERT INTO students (student_code, name, email, address) VALUES (%s, %s, %s, %s)"
    val = (student_code, name, email, address)
    
    try:
        cursor.execute(sql, val)  # ดำเนินการ SQL statement
        mydb.commit()  # ยืนยันการเพิ่มข้อมูล
        print(f"เพิ่มข้อมูลสำเร็จ, ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"เกิดข้อผิดพลาด: {err}")
    finally:
        cursor.close()  # ปิด cursor
        mydb.close()  # ปิดการเชื่อมต่อกับฐานข้อมูล

# เรียกใช้ฟังก์ชันเพื่อเพิ่มข้อมูล
insert_student("2222", "ff", "rr@ku.th", "58")
