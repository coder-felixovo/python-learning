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

sql1 = "DELETE FROM anime_role WHERE name = '岩户铃芽'"

cursor.execute(sql1)

# 提交事务
db.commit()

print(cursor.rowcount)

sql2 = "SELECT * FROM anime_role"

cursor.execute(sql2)

result = cursor.fetchall()

for x in result:
    print(x)

sql3 = "DROP database IF EXISTS python_connect_mysql"

cursor.execute(sql3)

print(cursor)