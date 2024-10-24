tip=int(input("Enter your tip in % pick 15, 18, 20 or more than 20: "
))

if tip == 15:
    print("Standard")
elif tip == 18:
    print("Good")
elif tip == 20:
    print("Great")
else:
    print("Pick a right choice!")