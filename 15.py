#日期转换
months=["January","February","March","April","May","June","July","August","September","November","December"]
endings=["st","th","rd"]+17*["th"]\
        +["st","th","rd"]+7*["th"]\
        +["st"]
year=input("Year:");
month=input("Month (1-12):")
day=input("Day (1-31):")
month_number=int(month)
day_number=int(day)
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]
print(month_name+' '+ordinal+','+year)

