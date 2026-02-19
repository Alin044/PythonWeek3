import datetime

date = datetime.date(2025, 1, 13)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

print(date)
print(today)
print(time)
print(now)


target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
curent_datetime = datetime.datetime.now()

if target_datetime < curent_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
    