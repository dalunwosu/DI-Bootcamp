# Exercise 1
my_fav_numbers = set()
my_fav_numbers.add(7)
my_fav_numbers.add(10)
my_fav_numbers.add(21)
my_fav_numbers.add(69)
my_fav_numbers.add(304)
print(my_fav_numbers)
my_fav_numbers.add(66)
my_fav_numbers.add(79)
print(my_fav_numbers)
my_fav_numbers.remove(21)
print(my_fav_numbers)
friend_fav_numbers = set()
friend_fav_numbers.add(58)
friend_fav_numbers.add(25)
friend_fav_numbers.add(123)
friend_fav_numbers.add(98)
friend_fav_numbers.add(789)
friend_fav_numbers.add(69)
friend_fav_numbers.add(7)
friend_fav_numbers.add(10)
friend_fav_numbers.add(304)
friend_fav_numbers.add(21)
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2
# No. It is not possible to add anything to a tuple

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(0)
basket.pop(-1)
print(basket)
basket.insert(0, "Kiwi")
basket.insert(-1, "Apples")
print(basket)
count = basket.count("Apples")
print(count)
basket.clear()
print(basket)

# Exercise 4 
# A float is a number with a decimal point.
# The difference between and integer and float is that a float has a decimal point while an integer does not.
# 
num = 1.5 
num_list = [num]
for i in range(7):
    num += 0.5
    num_list.append(num)

print(num_list)

# Exercise 5 
number = 0
for n in range(20):
    number+= 1
    print(number)

digit = 0
for d in range(20) :
    digit += 1
    if digit % 2 == 0:
        print(digit)

# Exercise 6
my_name = "Dalu"
name = input("What is your name? ")
while True: 
    if name == my_name :
        print("Welcome Dalu")
        break
    else: 
        wrong = input("Sorry wrong name. What's your name?")
        if wrong == my_name:
            print ("Welcome Dalu")
            break
       





#Exercise 7
fruits = input("What are your favorite fruits? Note:give a space between each fruit: ")
print(fruits)
fruit_list = list[fruits]
print(fruit_list)
#fruit_list.append(fruits)
question = input("Give me any fruit: ")

if question in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

#Exercise 8 
price = 10
toppings_price = 0
topping = []
while True :
    toppings = input("What Toppings would you like on your pizza? (Type quit to stop): ")
    if toppings == "quit":
        break
    print("I'll add" + " " + toppings + " " + "to your pizza")
    toppings_price += 2.5
    topping.append(toppings)
Total = price + toppings_price
print("Your pizza will contain the following toppings" + " " + str(topping))
print("The Price of the pizza is $" + str(price) + " " + "The total price for toppings is $" + str(toppings_price) + " " + "The Total Amount is $" + str(Total)  )   

#Exercise 9
ticket_price = 0
Total_cost = 0
while True:
    family_age = int(input("What is your age? (Type done to stop): "))
    if family_age == -1 :
        break
    if family_age < 3:
        ticket_price = 0
    elif 3<= family_age <= 12 :
        ticket_price = 10
    elif family_age > 12:
        ticket_price = 15 
    Total_cost += ticket_price
print("The total ticket cost for your family is $" + str(Total_cost))

teens = ["Dalu", "Isaac", "Steph", "Joshua", "Goke", "Uche", "Tom","Zara","Ife","Karsten"]
permitted_teens = []

for teen in teens:
    age = int(input("What is " + teen + "'s age? "))
    if 16 <= age <= 21:
        permitted_teens.append(teen)

print("The following teenagers are permitted to watch the movie: " + str(permitted_teens))

# Exercise 10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("All sandwiches have been made. Here is a list of finished sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

#Exercise 11
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("The deli has run out of pastrami.")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("All sandwiches have been made. Here is a list of finished sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
