names = "files/names.txt"
with open(names,"r") as f:
    name = f.readlines()
    fifth = name[4]
    f.seek(0)
    characters = f.read()

print(name)
print(fifth)
print(characters)