import re
import math

string = input()
food_pattern = r'([\#\|]{1})([a-zA-Z\s]+)\1' \
               r'([0-3]{1}[1-9]{1})[\/]{1}[0-1]{1}[0-9]{1}[\/]{1}[0-9]{1}[0-9]{1}' \
               r'\1[1-9]+[0-9]{0,4}\1'

food_match = re.finditer(food_pattern, string)
item_date_calo_list = []
food_list = []
best_date_list = []
nurtrition_list = []
total_calo = 0

for i in food_match:
    item_date_calo = i.group()
    if "#" in item_date_calo:
        item_date_calo_list = re.split("#", item_date_calo)
    elif "|" in item_date_calo:
        item_date_calo_list = re.split(r"\|", item_date_calo)
    item_date_calo_list = [i for i in item_date_calo_list if i != ""]
    food_list.append(item_date_calo_list[0])
    best_date_list.append(item_date_calo_list[1])
    nurtrition_list.append(item_date_calo_list[2])
    total_calo += int(item_date_calo_list[2])

print(f"You have food to last you for: {math.floor(total_calo/2000)} days!")
for i in range(len(food_list)):
    print(f"Item: {food_list[i]}, "
          f"Best before: {best_date_list[i]}, "
          f"Nutrition: {nurtrition_list[i]}")

# https://judge.softuni.org/Contests/Practice/Index/2525#1

# Problem 2 - Ad Astra
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#1.
#
# You are an astronaut who just embarked on a mission across the solar system. Since you will be in space for a long time, you have packed a lot of food with you. Create a program, which helps you identify how much food you have left and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. You must extract the information about the food and calculate the total calories.
# First, you must extract the food info. It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace
# •	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
# •	The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.
# Input / Constraints
# •	You will receive a single string
# Output
# •	First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# •	The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"
# Examples
# Input
# #Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|
# Output	Comments
# You have food to last you for: 2 days!
# Item: Bread, Best before: 19/03/21, Nutrition: 4000
# Item: Apples, Best before: 08/10/20, Nutrition: 200
# Item: Carrots, Best before: 06/08/20, Nutrition: 500	We have a total of three matches – bread, apples, and carrots.
# The sum of their calories is 4700. Since you need 2000kcal a day, we divide 4700/2000, which means this food will last you for 2 days.
# We print each item
# Input
# $$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|
# Output	Comments
# You have food to last you for: 9 days!
# Item: Fish, Best before: 24/12/20, Nutrition: 8500
# Item: Ice Cream, Best before: 03/10/21, Nutrition: 9000
# Item: Milk, Best before: 05/09/20, Nutrition: 2000	We have three matches. The total calories are 8500 + 9000 + 2000 = 19500, which means you have food for a total of 9 days.
# Input
# Hello|#Invalid food#19/03/20#450|$5*(@
# Output	Comments
# You have food to last you for: 0 days!	We have no matches, which means we have no food.
# The colored text is not a match since it doesn't have a # at the end.
# JS Examples
# Input
# [
# '#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|'
# ]
# Output	Comments
# You have food to last you for: 2 days!
# Item: Bread, Best before: 19/03/21, Nutrition: 4000
# Item: Apples, Best before: 08/10/20, Nutrition: 200
# Item: Carrots, Best before: 06/08/20, Nutrition: 500	We have a total of three matches – bread, apples, and carrots.
# The sum of their calories is 4700. Since you need 2000kcal a day, we divide 4700/2000, which means this food will last you for 2 days.
# We print each item
# Input
# [ '$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|' ]
# Output	Comments
# You have food to last you for: 9 days!
# Item: Fish, Best before: 24/12/20, Nutrition: 8500
# Item: Ice Cream, Best before: 03/10/21, Nutrition: 9000
# Item: Milk, Best before: 05/09/20, Nutrition: 2000	We have three matches. The total calories are 8500 + 9000 + 2000 = 19500, which means you have food for a total of 9 days.
# JavaScript Input
# ['Hello|#Invalid food#19/03/20#450|$5*(@' ]
# Output	Comments
# You have food to last you for: 0 days!	We have no matches, which means we have no food.
# The colored text is not a match since it doesn't have a # at the end.