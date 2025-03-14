# Per apple pie =
pie_crust_per_pie = 1 
flour_per_pie = 2 
apples_per_pie = 6 
cinnamon_per_pie = 3/4 
sugar_per_pie = 3/4 
salt_per_pie = 1/4  
nutmeg_per_pie = 1/8 
lemon_juice_per_pie = 1 

number_of_pies = input("How many pies do you need: ")
number_of_pies = int(number_of_pies)

print("Boxs of pie crust", (number_of_pies * pie_crust_per_pie))
print("flours of tsp", (number_of_pies * flour_per_pie))
print("apples", (number_of_pies * apples_per_pie))
print("tsp of cinnamon", (number_of_pies * cinnamon_per_pie))
print("cups of sugar", (number_of_pies * sugar_per_pie))
print("tsp of salt", (number_of_pies * salt_per_pie))
print("tsp of ground nutmeg", (number_of_pies * nutmeg_per_pie))
print("tsp of lemon juice", (number_of_pies * lemon_juice_per_pie))