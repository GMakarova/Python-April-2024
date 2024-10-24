count = 0
limit = 10

while count < limit:
    print(count)
# 1) 0 < 10, print(0)
# 2) 0 < 10, print(0)
# 3) 0 < 10, print(0)

    count = count + 1
# 1)  0 < 10,            print(0 < 10) = 0 True
# 2)  count = 1,         print(1 < 10) = 1 True
# 3)  count= 1 + 1 = 2,  print(2 < 10) = 2 True
# 4)  count= 2 + 1 = 3,  print(3 < 10) = 3 True
# 4)  count= 3 + 1 = 4,  print(4 < 10) = 4 True
# ....
# 9)  count= 7 + 1 = 8,  print(8 < 10) = 9 True
# 10) count= 9 + 1 = 10, print(10 < 10) = False