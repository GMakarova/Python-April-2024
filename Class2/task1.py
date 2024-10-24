age=int(input("Enter your age: "))

if age<13 and age>0:
    print("Child")
elif age>=13 and age<18:
    print("Teenager")
elif age>=18 and age<65:
    print("Adult")
elif age>=65:
    print("Elder")