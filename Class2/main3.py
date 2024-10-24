years=input("Enter number of years: ")
unit=int(input("""Pick your choice: 
1-Days
2-Weeks
3-Hours
"""))

if unit == 1:
    print(f"{years*365} days")