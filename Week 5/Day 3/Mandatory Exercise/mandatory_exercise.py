#Exercise 1


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