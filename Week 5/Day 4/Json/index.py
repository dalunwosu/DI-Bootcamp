import json
family =  {}
json_file = "Json/file.json"
with open(json_file, 'r') as file:
    family = json.load(file)

print(family)

for child in family["children"]:
    child["favorite_color"] = "blue"
print(family)

with open(json_file,"w") as file:
    json.dump(family,file, indent= 4)
