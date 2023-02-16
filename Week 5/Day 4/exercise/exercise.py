names = "files/names.txt"
with open(names,"r") as f:
    characters = f.read()
    f.seek(0)
    name = f.readlines()

print(name)
print(characters)
print(f"The fifth line is: {name[4]}")
print(f"The first five characters are: {characters[:5]}")

darth = 0
luke = 0
lea = 0
for id in name:
    if id.strip("\n") == "Darth":
        darth += 1
    if id.strip("\n") == "Luke":
        luke += 1
    if id.strip("\n") == "Lea":
        lea += 1
print(darth)
print(luke)
print(lea)
    
with open(names,"a") as f:
    f.write("\nDalu")

print(characters)
print(name)

for i, title in enumerate(name):
    if title.strip("\n") == "Luke":
        name[i]= title.strip("\n") + "Skywalker\n"

with open (names,"w") as file:
    file.writelines(names)