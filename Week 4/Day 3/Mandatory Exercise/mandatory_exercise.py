# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for item in zip(keys,values):
    print(item)

# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
ticket_price = 0
total_price = 0
for names, ages in family.items():
    if ages<3:
        ticket_price = 0
    elif 3<=ages<=12:
        ticket_price = 10
    elif ages>12:
        ticket_price = 15
    total_price += ticket_price
    print(f"The ticket price for {names} is ${ticket_price}")
print(f"The total ticket price is {total_price} ")

# Exercise 3
brand = {
    "name":"Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home",],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color":{
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]
                }
}
print(brand)
brand["number_stores"] = 2
print("Zara's clients ")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    print("True")
    brand["international_competitors"].append("Desigual")
else:
    print("False")
print(brand)
del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())
more_on_zara = {
"creation_date": 1975, 
"number_stores": 10000
}
brand.update(more_on_zara)
print(brand)
print(brand["number_stores"]) #The value changed from 2 to 10,000, meaning it prioritizes the recent input

#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    disney_users_A[user] = i

print(disney_users_A)
disney_users_B = {}
for n, user in enumerate(users):
    disney_users_B[n] = user
print(disney_users_B)

disney_users_C = {} 

for j,user in enumerate(sorted(users)) : 
    disney_users_C[user] = j
print(disney_users_C)

disney_users_D = {}
l = 0
for user in users:
    if "i" in user:
        disney_users_D[user] = l
        l+=1
print(disney_users_D)
disney_users_E = {}
e = 0
for user in users:
    if user[0] in ["M","P"] :
        disney_users_E[user] = e
        e += 1
print(disney_users_E)





