def hello():
    print("Hello")

hello()

def world():
    print("Hello World!")

world()

# def hello(t, O):
def hello(t, O, x, y):
    # print("Hello", t)
    # print("Hello", O)
    # print("Hello", t, O)
    print("Hello", t, O, x, y)

# hello("Tim")
# hello("Ann")
# hello("Ben")
hello("Tim", "Ann", "Jenny", "Brad")

def sum(a,b):
    return a+b
print(sum(5,6))

def sum(a,b):
    return a-b
print(sum(9,4))