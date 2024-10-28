while True:
    age=int(input("Enter your age: "))
    if age < 13:
        print("Sorry, you are not allowed to enter!")
    elif age >= 13 and age < 18:
        print("Call your legal guardian")
    else: 
        print("You're Welcome!")