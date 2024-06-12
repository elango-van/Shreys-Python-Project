import time
# import datetime
# from datetime import datetime, date, timedelta
from datetime import datetime, date, timedelta
# import datetime
# seconds = 30
# starttime = time.time()
# print(starttime)
# while True:
#     now = time.time()
#     if now > starttime + seconds:
#         break
#     print(now - starttime)

# When input has two-digit year instead of four-digit year
date_str = '23-03-01'
date_obj = datetime.strptime(date_str, '%y-%m-%d')
# Raises ValueError: time data '23-03-01' does not match format '%y-%m-%d'
print(date.today())
print(datetime.now())
# When the input has missing leading zeros for hour and minute
time_str = str(date.today()) + ' 15:30'
print(time_str)
time_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M')
# Raises ValueError: time data '8:30' does not match format '%H:%M'
print(time_obj)
if datetime.now() < time_obj:
    print("It's a trading time")
else:
    print("It's not a trading time")

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)

d = date(2024, 6, 12)
d= date.today()
next_monday = next_weekday(d, 3) # 0 = Monday, 1=Tuesday, 2=Wednesday...
print(next_monday)

today = datetime.today()
print(today + timedelta(days=1))
print((today + timedelta(days=1)).strftime('%Y-%m-%d %H:%M'))

print(" ******************************* ")
def time_counter(seconds):
    starttime = time.time()
    print(starttime)
    while True:
        now = time.time()
        if now > starttime + seconds:
            break
        yield now - starttime

for t in time_counter(20):
    print(t)
    time.sleep(3)

