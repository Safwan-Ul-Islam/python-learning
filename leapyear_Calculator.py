year= int(input("write a year to check wheather its leap year or not"))
cal=year/4
check= year%4
if check==0:
    print(f" {year}/4= {cal} so it is a leap year")
else:
    print(f"{year}/4= {cal} so it is not a leap year")