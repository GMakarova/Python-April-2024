tip=int(input("""Your tip:
1-15%
2-18%
3-20%
"""))

if tip == 1:
    print("Standard")
elif tip == 2:
    print("Good")
elif tip == 3:
    print("Great")
elif tip > 20:
    print("My Hero!")