
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    # pass   #just tells python to pass so it has no empty class
   def bark(self):
       print("bark")

class Cat(Mammal):
    def bmows(self):
        print("mow")


dog1 = Dog()
cat1 = Cat()

 # inhertance