class Animal:
    def __init__(self,name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")



#inheritance in action
class Dog(Animal):
    pass

class cat(Animal):
    pass

class Mouse(Animal):
    pass

dog1 = Dog("Scooby")

cat1 = cat("Garfield")

mouse1 = Mouse("Jerry")


print(dog1.name)
dog1.eat()

mouse1.sleep()

#multiple inheritance

class LivingThing:
    def __init__(self,name):
        self.name = name
    def breathing(self):
        print("I am breathing.")


class Fish(Animal,LivingThing):
    pass

fish1 = Fish("Cherry")

fish1.eat()
fish1.breathing()
    
#multilevel Inheritance, Predator took inheritance from Animal and then Lion from Predator
class Predator(Animal):
    def hunting(self):
        print(f"{self.name} is hunting")


class Lion(Predator):
    pass

lion1 = Lion("Musafa")

lion1.hunting()

#Super() used in child class to call methods from a parent class which allows to extend the functionality of inherited method
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def desctibe(self):
        print(f"It is {self.color}.")

class Circle(Shape):
    def __init__(self,color,filled, radius):
        super().__init__(color,filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, side):
        super().__init__(color,filled)
        self.side = side

circle = Circle("red", True, 5)

print(circle.color)
circle.desctibe()

