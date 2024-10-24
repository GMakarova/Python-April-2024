def days(years):
    day = years * 365
    return day

def weeks(years):
    week = years * 52
    return week

def months(years):
    month = years * 12
    return month

def hours(years):
    hour = years * 365 * 24
    return hour

years = int(input("Enter number of years: "))

print(f"In {years} years there are {days(years)} days")
print(f"In {years} years there are {weeks(years)} weeks")
print(f"In {years} years there are {months(years)} months")
print(f"In {years} years there are {hours(years)} hours")

# print(days())
# print(weeks())
# print(months())
# print(hours())