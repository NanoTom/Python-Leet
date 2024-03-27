#very very basic just testing the water for date manipulation

import calendar

def count_days(year, month, whichday):
    count = 0
    day = calendar.Calendar(whichday).monthdayscalendar(year,month) # imp
    for x in day:
        print(x)
        if (x[whichday]!=0):
            count = count+1
    return count


year = int(input("Which year you would like? (ex 2024): "))
month = int(input("Which month would you like (ex 6): "))
days = int(input("Which day would you like (depends on your system)"))


daysofweek = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
dayname = daysofweek[days]

print("There are:,",count_days(year,month,days), dayname+"'s","in that month and year")