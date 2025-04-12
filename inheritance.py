# Simple Inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived Class(Child Class)

class Dog(Animal):

    def speak1(self):
        print(f"{self.name} barks")

# Create an Instance of the Animal Class
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound 


# Create an Instance of the Dog Class
dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks
