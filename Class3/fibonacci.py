# 0 1 1 2 3 5 8 13 21 34 55 89

limit=int(input("Enter the limit: "))

first=0
second=1
print(first)
print(second)

next=first+second

while next <= limit:
    print(next)
    first=second
    second=next
    next=first+second

#0 1 1 2 3 5 8 13
#first=0
#secound=1
#next=1