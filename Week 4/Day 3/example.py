sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict["class"]["student"]["marks"]["history"])

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
print(sample_dict)
keys_to_remove = ["name", "salary"]

n = 0
for i in keys_to_remove[0:]:
    del sample_dict[keys_to_remove[n]]
    n += 1
print(sample_dict)