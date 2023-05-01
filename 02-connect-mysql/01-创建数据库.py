import mysql.connector

# 创建连接
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)

# print(db)

# 创建指针
cursor = db.cursor()

sql1 = "CREATE DATABASE IF NOT EXISTS python_connect_mysql CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"

cursor.execute(sql1)

sql2 = "SHOW DATABASES;"

cursor.execute(sql2)

for x in cursor:
    print(x)
