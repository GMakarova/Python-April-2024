years=int(input("Enter number of years: "))
unit=int(input("""Pick your choice: 
1-Days
2-Weeks
3-Hours
"""))

if unit == 1:
    print(f"{years*365} days")
elif unit == 2:
    print(f"{years*53} weeks")
elif unit == 3:
    print(f"{years*365*24} hours")
else:
    print("Pick a right choice.")