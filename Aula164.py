# Formatando datas do datetime
# datetime.strptime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2002, 7, 5, 9, 30, 20)
data = datetime.strptime('2002-7-5 9:30:20', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)
