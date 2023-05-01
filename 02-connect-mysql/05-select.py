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

sql1 = "SELECT * FROM anime_role"

cursor.execute(sql1)

result = cursor.fetchall()

for x in result:
    print(x)