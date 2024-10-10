import mysql.connector

# เชื่อมต่อกับฐานข้อมูล
connection = mysql.connector.connect(
    host="localhost",        # ชื่อโฮสต์ฐานข้อมูล
    user="root",    # ชื่อผู้ใช้ MySQL
    password="", # รหัสผ่าน MySQL
    database="students" # ชื่อฐานข้อมูล
)

# สร้าง cursor สำหรับการสั่ง SQL
cursor = connection.cursor()

# คำสั่ง SQL สำหรับดึงอีเมลและแยกตามโดเมน
query = """
    SELECT email, SUBSTRING_INDEX(email, '@', -1) AS domain
    FROM students
    ORDER BY domain ASC;
"""

# รันคำสั่ง SQL
cursor.execute(query)

# ดึงข้อมูลทั้งหมดที่ได้จากการ query
results = cursor.fetchall()

# จัดกลุ่มและแยกอีเมลตามโดเมน
emails_by_domain = {}



for (email, domain) in results:
    if domain not in emails_by_domain:
        emails_by_domain[domain] = []
    emails_by_domain[domain].append(email)

# แสดงผลลัพธ์
for domain, emails in emails_by_domain.items():
    print(f"Domain: {domain} : จำนวน {len(emails)}")
    for email in emails:
        print(f"  - {email}")
    print()

# ปิด cursor และการเชื่อมต่อฐานข้อมูล
cursor.close()
connection.close()
  
