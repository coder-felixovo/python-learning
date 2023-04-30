import datetime

date = datetime.datetime.now()
print(date)  # yyyy-mm-dd hh:mm:ss.ms
print(date.year)
print(date.strftime("%A"))  # weekday

# 使用datetime()创建日期对象
date = datetime.datetime(2023, 2, 25)
print(date)

# 使用strftime()方法返回指定格式
print(date.strftime("%B"))  # month


