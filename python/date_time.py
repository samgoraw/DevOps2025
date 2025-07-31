import datetime

now = datetime.datetime.now()
print("Current date & time:",now)
print("Current date only:",datetime.date.today())

d=datetime.date(2023,12,15)
print('Specific Date:', d)
t=datetime.time(14,30,15)
print(t)


print('Year: ',now.year)
print('Month: ',now.month)
print('day: ',now.day)
print('hour: ',now.hour)
print('Minute: ',now.minute)

# formate Date (strftime)
formatteddate = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatteddate)

#parse(strptime) string to date
date_str = "2025-05-03"
date_obj = datetime.datetime.strptime(date_str,"%Y-%m-%d")
print(date_obj)