# class cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print("i am a cat my name is",self.name,"my age is",self.age)

#     def makesound(self):
#         print("meow")

# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print("i am a dog my name is",self.name,"my age is",self.age)

#     def makesound(self):
#         print("bow")

# cat1=cat("lalitha",15)
# dog1=dog("harish",16)

# for animal in(cat1,dog1):
#     animal.info()
#     animal.makesound()

# activity 2

class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("selling price is",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price

c=computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(1000)
c.sell()