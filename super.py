# Base Class

class Animal:
    def __init__(self):
        self.name = "Bunny"

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived Class(Child Class)

class Dog(Animal):
    def __init__(self,breed):
        self.breed = breed
        super().__init__()

    def speak1(self):
        super().speak() # call parent(base) class method
        print(f"{self.name} barks. & Breed is {self.breed}")

# Create an Instance of dog Class
dog = Dog("Labrador")
dog.speak1() # Output: Bunny makes a sound. Labrador barks. & Breed is  Labrador