#Exe
class Family:
    def __init__(self,members:list,last_name:str):
        self.members = members
        self.lastname = last_name
    def born (self,**new_child):
        self.members.append(new_child)
        print(self.members)
        print("Congratulations on the birth of your child!")
    def is_18 (self,name):
        for member in self.members:
            if name == member["name"] and member["age"]>=18:
                return True 
            else:
                return False
    def family_presentation(self):
        print("The last name of the family is",self.lastname)
        print("The members of the family are:")
        for member in self.members:
            print(member["name"])

group = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}],"Jordan")
group.born(name ="Johnny",age = 0, gender = "Male",is_child = True)
print(group.is_18("Michael"))
group.family_presentation()

#Exercise 2
class TheIncredibles(Family):
    def __init__(self, members: list, last_name: str):
        super().__init__(members, last_name)
    def use_power(self):
        for member in self.members:
            if member["age"]>18:
                print(member["power"])
            else : 
                print(member["name"],"is not 18 years old yet")
    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(member)

incredible = TheIncredibles([{'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}],"Incredible")
incredible.use_power()
incredible.incredible_presentation()
incredible.born(name = "Baby Jack",age = 0, gender = "Male",is_child = True, power = "Unknown Power",incredible_name = "Jack Jack")
incredible.incredible_presentation()
incredible.use_power()