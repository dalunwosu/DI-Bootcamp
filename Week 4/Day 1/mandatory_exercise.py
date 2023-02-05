#Exercise 1
Hello = ("Hello World\n")*4
print(Hello)

#Exercise 2
Calculate = (99^3)*8
print(Calculate)

#Exercise 3
part1 = 5 < 3 #false
part2 = 3 == 3 #true
part3 = 3 == "3" #false
#part4 = "3" > 3 #false
part5 = "Hello" == "hello" #false
print(part1)
print(part2)
print(part3)
#print(part4)
print(part5)

#Exercise 4
computer_brand = "HP Omen 16"
print("I have a" + " "+ computer_brand + " " + "computer")

#Exercise 5
name = "Dalu"
age = "17"
shoe_size = "47"
info = ("My name is" +" " + name + " " + "I am" + " " + age + " " + "years old" + " "  + "and my shoe size is" + " " + shoe_size)
print(info)

#Exercise 6
a = 69
b = 21
if a > b: 
    print("Hello World")

#Exercise 7 
number = int(input("Number:"))
if number % 2 == 0 :
    print("even")
else:
    print("odd")

#Exercise 8
your_name = input("What is your name?")
if your_name == name:
    print("Oh, we have the same name. What're the odds of that. Mine's still better though")
else: 
    print("We don't have the same name. I mean obviously what're the odds you'll find someone with the name Dalu")

#Exercise 9
inch = int(input("What is your height in inches: "))
centimetre = inch * 2.54
if centimetre > 145:
    print("You are tall enough to go on the ride")
else: 
    print("You are too short, please grow some more")
