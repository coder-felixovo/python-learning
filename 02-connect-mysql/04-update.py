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

sql1 = "UPDATE anime_role SET address = '九州-update' WHERE name = '岩户铃芽'"

cursor.execute(sql1)

# 提交事务
db.commit()

print(cursor.rowcount)