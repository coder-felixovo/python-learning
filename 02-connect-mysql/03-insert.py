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

sql1 = "INSERT INTO anime_role (name, address) VALUES (%s, %s)"

params = ('岩户铃芽', '九州')

cursor.execute(sql1, params)

# 提交事务
db.commit()

print(cursor.rowcount)
