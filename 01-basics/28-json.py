# 导入内置模块json
import json

jsonData = '{"brand":"Porsche", "year": 1963}'

parseResult = json.loads(jsonData)
print(type(parseResult))  # dict
print(parseResult["brand"])  # Porsche

# object => json string
car = {
    "brand": "Porsche",
    "model": 911,
}
carJsonStr = json.dumps(car)
print(type(carJsonStr))  # <class 'str'>

