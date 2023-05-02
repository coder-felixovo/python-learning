from django.db import models

# Create your models here.

# 类名 --- 表名
# 属性 --- 表中的列名
# CharField --- varchar
# DateField --- datetime
class Person(models.Model):
    name = models.CharField(max_length=20)
