import calendar

print()
print(calendar.weekheader(3)) # j koyta nite chai 4 example 1 mean 1 letter 2 means 2 ,3 means mon
print() # neq line

print(calendar.firstweekday()) # 1st day monday and python e monday thkei day shuru hoy normally amio tai dilam monday=0
print()
print("\n")

for name in calendar.day_name: # day name nibo sob
    print(name)
    print()

for name in calendar.month_name: # month name
    print(name)
    print()


print(calendar.month(2020, 7)) # j year er j month ta chai ta hobe
print()

# print(calendar.monthcalendar(2020, 7))

print(calendar.calendar(2020)) # pura 2020 er calender chole ashbe sob ashbe sob just bom blast hoe jay

# day = input()
# month = input()
# year = input()

day_of_the_week = calendar.weekday(2020, 8, 3) # just mention kri j kon year er kon month and kon day
print(day_of_the_week) # and day ta print kore
print()
is_leap = calendar.isleap(2020) # just check kri j year ta leap year naki na
print(is_leap) # leap naki ta print kori..