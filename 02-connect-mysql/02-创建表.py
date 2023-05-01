import mysql.connector

# 创建连接
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="python_connect_mysql"  # 指定数据库
)

# 创建指针
cursor = db.cursor()

sql1 = """
CREATE TABLE IF NOT EXISTS anime_role (
    id INT(1) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10),
    address VARCHAR(10)
);
"""

cursor.execute(sql1)

sql2 = "SHOW TABLES;"

cursor.execute(sql2)

for x in cursor:
    print(x)

