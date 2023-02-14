#Exercise 1

class functions :
    """This is a function which prints the results of the in-built functions abs(), int() and input() """
    def built_in_functions(self):
        num = 5.678787869686989585968688
        dig = abs(num)
        print(dig)

        num_string = "1623463737829293947"
        num_int = int(num_string)
        print(num_int)

        statement = "My name is Chukwudalu Nwosu, I am 17 years old, I live in Tel Aviv and I am a stduent of Developer's Institute"
        inp= input(statement)
        print(inp)


functions.built_in_functions(0)
print(functions.__doc__)





#Exercise 2
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return(f"{self.amount} {self.currency}s")
    def __int__(self):
        return self.amount
    def __repr__(self):
        return str(self) + " " + str(id(self))
    def __add__(self,value):
        if isinstance(value,int):
            return self.amount + value
        if isinstance(value,Currency):
            if self.currency == value.currency:
                return self.amount + value.amount
            else:
                raise TypeError(f" Cannot add between Currency type {self.currency} and {value.currency}")    
    def __iadd__(self,value):
        if isinstance(value,int):
             self.amount += value
        if isinstance(value,Currency):
            if self.currency == value.currency:
                self.amount += value.amount
            else:
                raise TypeError(f" Cannot add between Currency type {self.currency} and {value.currency}")
        return self
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1+c2)
c1 += c2
print(c1)
c1 += 5
print(c1)