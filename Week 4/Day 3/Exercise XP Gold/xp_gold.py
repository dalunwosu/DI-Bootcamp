birthdays = {
    "Dalu": "2005/11/14",
    "Isaac": "2004/12/30",
    "Uche": "2005/8/15",
    "Joshua": "2006/7/26",
    "Goke": "2006/9/28"
}
print(birthdays)
print("You can look up the birthdays of the people in the list!")

day = input("Person Name: ")

birthday = birthdays.get(day, f"There is no {day} in the data")
print(birthday)