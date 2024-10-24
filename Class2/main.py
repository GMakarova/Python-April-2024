x=5
y=6

print(x==5) # 5 = 5
print(y==6) # 6 = 6
print(x>y)  # 5 > 6
print(y>=x) # 6 >= 5

print(x!=y) # 5 not equal 6
print(x>4 and y<7)  # True and True
print(x>5 and y<7)  # False and True
print(x>3 and y!=7) # True and True
print(x>3 and y!=6) # True and False
print(x>10 and y<3) # False and False

print(x>4 or y<7)  # True and True
print(x>5 or y<7)  # False and True
print(x>3 or y!=7) # True and True
print(x>3 or y!=6) # True and False
print(x>10 or y<3) # False and False

print(not(x>3))                     # True
print(not(not(x>3)))                # False
print(not(not(not(x>3))))           # True
print(not(not(not(not(not(x>3)))))) # False