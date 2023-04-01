# built-in module `json`
import json

jsonData = '{"name":"Bill", "age":63, "city":"Seatle"}'

parseResult = json.loads(jsonData)
print(type(parseResult))  # dict
print(parseResult["name"])

# object => json string
car = {
    "brand": "Porsche",
    "model": 911,
    "price": "300W"
}
print(type(car))  # dict
carJsonStr = json.dumps(car)

