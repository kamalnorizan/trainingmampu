import calendar

cal = calendar.month(2021, 11)
print(cal)

yearcal = calendar.calendar(2022)
print(yearcal)

leapcheck = calendar.isleap(2024)
print(leapcheck)

leapday = calendar.leapdays(2000,2025)
print(leapday)