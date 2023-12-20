# Object-Oriented Programming (OOP)

# Class definition
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the sound method


# Inheritance
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Object instantiation
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")


# Polymorphism
def animal_sounds(animal):
    return animal.make_sound()


print(f"{dog_instance.name} says: {animal_sounds(dog_instance)}")
print(f"{cat_instance.name} says: {animal_sounds(cat_instance)}")


# Encapsulation and Abstraction
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make_model(self):
        return f"{self.__make} {self.__model}"


# Instantiating a Car object
my_car = Car("Toyota", "Camry")
print("Car details:", my_car.get_make_model())
