# the ingredients and amounts needed for 1 apple pie
pie_crust_per_pie = 1 # 1 box of pie crust
flour_per_pie = 2 # tablespoons of flour
apples_per_pie = 6 # apples
cinnamon_per_pie = 3/4 # teaspoons of ground cinnamon
sugar_per_pie = 3/4 # cup of sugar
salt_per_pie = 1/4 # teaspoon of salt 
nutmeg_per_pie = 1/8 # teaspoon of ground nutmeg
lemon_juice_per_pie = 1 # teaspoon of lemon juice

# user enters the number of pies needed
num_pies = int (input("Enter the number of pies needed:"))

#calculate the total amount of each ingredient needed
total_pie_crust = pie_crust_per_pie * num_pies
total_flour = flour_per_pie * num_pies
total_apples = apples_per_pie * num_pies
total_cinnamon = cinnamon_per_pie * num_pies
total_sugar = sugar_per_pie * num_pies
total_salt = salt_per_pie * num_pies
total_nutmeg = nutmeg_per_pie * num_pies
total_lemom_juice = lemon_juice_per_pie * num_pies

# Output the total amounts of each ingredient 
print(f"To make {num_pies} apple pies, you will need:")
print(f"{total_pie_crust} box(es) of pie crust")
print(f"{total_flour} tablespoons of flour")
print(f"{total_apples} apples")
print(f"{total_cinnamon} teaspoons of ground cinnamon")
print(f"{total_sugar} cups of sugar")
print(f"{total_salt} teaspoons of salt")
print(f"{total_nutmeg} teaspoons of ground nutmeg")
print(f"{total_lemon_juice} tablespoons of lemon juice")