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

years = float(input("Enter the number of years: "))
    
days = int(days(years))
weeks = int(weeks(years))
months = int(months(years))
hours = int(hours(years))
    
print(f"{years:.0f} years is approximly:")
print(f"{days} days")
print(f"{weeks} weeks")
print(f"{months} months")
print(f"{hours} hours")