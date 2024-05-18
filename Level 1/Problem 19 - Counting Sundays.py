# Counting Sundays

# if the first of the month is 0 mod 7 then its a sunday

from datetime import date

count = 0
for year in range(1901, 2001):
    for month in range(1,13):
        d = date(year=year, month=month, day=1)
        if d.weekday() == 1:
            count += 1
        print(year, month)
print(count)