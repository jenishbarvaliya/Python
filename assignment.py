# 0. addition of two number
a=2
b=3
c=a+b
print(c) # output:

# 4. 
# Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
street = 'kamrej'
city = 'surat'
country = 'india'

address = street+"\n"+city+"\n"+country
print(address)
address = f'{street}\n{city}\n{country}'
print(address)

# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
s= "Earth revolves around sun"
print(s[7:15])
print (s[-3:])

# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
vegi = 10
fruit = 5
s = f'i Eat eavry day {vegi} vegitables and {fruit} fruits'
print (s)

# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
s='maine 200 banana khaye'
newS = s.replace("banana","samosa").replace("200","10")
print(newS)

# 5.
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

exp = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
extra = exp[1]-exp[0]
print(extra)

# 2. Find out your total expense in first quarter (first three months) of the year.
fQuater =exp[0]+exp[1]+exp[2]
print(fQuater)

# 3. Find out if you spent exactly 2000 dollars in any month
print(2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print (exp)

# 5. You returned an item that you bought in a month of April and
exp[3] = exp[3]-200
print(exp)

# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["doctor Strange"]
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

# 8.
# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("enter the name of city : ")

if city in india:
    print("city belongs to india")
elif city in pakistan:
    print("city belongs to pakistan")
elif city in bangladesh:
    print("city belongs to bangladesh")
else:
    print("city not found")

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("enter the first city : ")
city2 = input("enter the second city : ")

if city1 in india:
    if city2 in india:
        print("Both city in india")
    else:
        print("They don't belong to same country")
elif city1 in pakistan:
    if city2 in pakistan:
        print("Both city in pakistan")
    else:
        print("They don't belong to same country")
elif city1 in bangladesh:
    if city2 in bangladesh:
        print("Both city in bangladesh")
    else:
        print("They don't belong to same country")
else:
    print("They don't belong to same country")

# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal
sLevel = int(input("Enter the Fasting sugar level : "))
# If it is below 80 to 100 range then print that sugar is low
if sLevel < 80:
    print("Sugar level is low")
elif sLevel>100:
    print("Sugar level is high")
else:
    print("Sugar level is normal")

# 9.
# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

heads = 0
for i in result:
    if i == "heads":
        heads=heads+1

print(heads)

# Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    if i % 2 != 0:
        print(pow(i,2))

# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["january", "february","march","april","may"]

amount = int(input("Enter the amount "))
month = -1

for i in range(len(expense_list)):
    if amount == expense_list[i]:
        month = i
        break

if month != -1:
    print(f"You spent {amount} in {month_list[month]}")
else:
    print("Amount not found in the list")

# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
for i in range(5):
    print(f"Completed {i+1} km")
    response = input("Are you tired? say yes or no : ")
    if response.lower() == "yes":
        print("You are tired, you didn't finish the rac")
        break
    else:
        print("You are not tired, keep going")

    if i == 4:
        print("You have completed the race, congratukations!!")  # This will only print after the loop finishes,

# Write a program that prints following shape

# *
# **
# ***
# ****
# ***** hollow 

row = int(input("Enter the number of raws you want print : "))

for i in range(1,row+1):

    for k in range(row-i):
        print(" ",end=" ")
    for j in range(2*i - 1):
        if j == 0 or j == 2*i -2:
            print("*",end=" ")
        else:
            if i== row:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print("\n")

# 10.
# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height
def calculate_area(b,h):
    return 0.5 * b * h

print(calculate_area(3,5))

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
def calculate_area(b,h,shape):
    if shape.lower() == "triangle":
        return 0.5 * b * h
    elif shape.lower() == "rectangle":
        return b * h
    else:
        return "Invalid shape"

b = int(input("Enter the value of bace : "))
h = int(input("Enter the value of height : "))
shape = input("Enter the shape (triangle/rectangle) : ")
print(calculate_area(b,h,shape))

# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
def print_pattern(row):
    for i in range(1,1+row):
        for j in range(1,row+1):
            if j <= i:
                print("*",end=" ")
        print("\n")

row = int(input("Enter the number of rows : "))
print_pattern(row)  

# We have following information on countries and their population (population is in crores),

# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21

population = {
    "chaina" : 143,
    "india" : 136,
    "usa" : 32,
    "pakistan" : 21
}

def print_all():
    for country,p in population.items():
        print(f"{country} ==> {p}")

print_all()

# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
def add():
    country = input("enter the name of country which you want to add in dictionary : ")
    country = country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p = float(input(f"enter the population of the company{country}"))
    population[country]=p
    print_all()
