foods=("Apple","Banana","Orange","Mango","Strawberry","Grape","Mandrine","Strawberry")
calories=(52,96,62,60,33,68,50,33)

print(foods)
print(calories)

foods_list=list(foods)
calories_list=list(calories)

print(foods_list[4])
print(calories_list[4])

print(foods_list[-2])
print(calories_list[-2])

uniq=set(foods_list)
print(uniq)

dict_foods={"Apple":52,"Banana":96,"Orange":62,"Mango":60,"Strawberry":33,"Grape":68,"Mandrine":50,"Strawberry":33}

dict_foods["Tomato"]=60
print(dict_foods)

dict_foods["Grape"]=50
print(dict_foods)