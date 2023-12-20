# Object-Oriented Programming (OOP) - Continued

# Composition
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"


class CarWithComposition:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__engine = Engine()  # Composition - CarWithComposition has an Engine

    def get_make_model(self):
        return f"{self.__make} {self.__model}"

    def start_engine(self):
        return self.__engine.start()

    def stop_engine(self):
        return self.__engine.stop()


# Instantiating a CarWithComposition object
my_car_composition = CarWithComposition("Honda", "Civic")
print("Car details:", my_car_composition.get_make_model())
print("Starting engine:", my_car_composition.start_engine())
print("Stopping engine:", my_car_composition.stop_engine())


# Decorators and Class Methods
class MyClass:
    class_variable = 0  # Class variable shared among all instances

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    def display_variables(self):
        print(f"Class variable: {self.class_variable}, Instance variable: {self.instance_variable}")


# Instantiating MyClass objects
obj1 = MyClass(10)
obj2 = MyClass(20)

MyClass.increment_class_variable()  # Incrementing the class variable
obj1.display_variables()
obj2.display_variables()


# Magic Methods (Dunder Methods)
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Overloading the '+' operator
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        # Overloading the 'str()' method for a readable string representation
        return f"{self.real} + {self.imag}j"


# Using the ComplexNumber class with magic methods
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
result = c1 + c2
print("Complex number addition result:", result)
