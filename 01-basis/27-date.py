import datetime

date = datetime.datetime.now()
print(date)  # yyyy-mm-dd hh:mm:ss.ms
print(date.year)
print(date.strftime("%A"))  # weekday

# Use `datetime()` to create date object.
date = datetime.datetime(2023, 2, 25)
print(date)

# Use `strftime()` to format the date object to a readable string.
print(date.strftime("%B"))  # month


