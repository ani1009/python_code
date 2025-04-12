# Single or Basic Inheritance

# Base Class

class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")


# Derived Class(Child Class)

class Child(Parent):
    def play(self):
        print(f"{self.name} is playing!")

# Create an Instance Of Child Class

child = Child("Aniket")

child.greet()  # Output: Hello, Aniket!

child.play()  # Output: Aniket is playing!

#-------------------------------------------------------------------------------------------------------------------------------

# Multiple Inheritance:

# Base Class:
class Grandparent:
    def __init__(self,name):
        self.name = name
        
    def tell_story(self):
        print(f"{self.name} tells a Story!")

# Intermidiate Class:
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working!")

# Derived Class(Child Class):
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing!")


# Create an Instance Of Child Class:

child = Child("Aniket")

child.tell_story()

child.work()

child.play()

#-------------------------------------------------------------------------------------------------------------------------

# Hierarchical Inheritance

# Base Class:

class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, My Name is {self.name}")

# Derived Class 1:

class Child1(Parent):
    def play(self):
        print(f"{self.name} is Playing")

# Derived Class 2:

class Child2(Parent):
    def study(self):
        print(f"{self.name} is Studying")

# Create Instance Of child 1 and Child 2 :

child_1 = Child1("Ram")

child_2 = Child2("Shyam")

child_1.greet()
child_1.play()

child_2.greet()
child_2.play()

#---------------------------------------------------------------------------------------------------------------------------

# Multiple Inheritance (Diamond Problem)

# Common Base Class:

class A:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello From A, {self.name}.")

# Intermidiate Class 1:

class B(A):
    def greet(self):
        print(f"Hello From B, {self.name}.")
        super().greet()

# Intermidiate Class 2:

class C(A):
    def greet(self):
        print(f"Hello From C, {self.name}.")
        super().greet()

# Derived Class :

class D(B,C):
    def greet(self):
         print(f"Hello From D, {self.name}.")
         super().greet()

# Create an Instance Of D:

d = D("Frank")
d.greet()

#-----------------------------------------------------------------------------------------------------------------------------

# Hybrid Inheritance:

# Base Class:

class Creature:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a Sound.")

# Intermidiate Class 1 (Hirarchical)

class Mamal(Creature):
    def feed(self):
        print(f"{self.name} is Feeding Milk")

# Intermidiate Class 2 (Multiple)

class Bird(Creature):
    def fly(self):
        print(f"{self.name} is Flying")

# Derived Class (Multiple Inheritance)

class Bat(Mamal, Bird):
    def __init__(self, name):
        Mamal().__init__(name) # Explicitly Calling the Constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal")

# Create an Instance of Bat:

bat = Bat("Bruce")

bat.sound()

bat.feed()

bat.fly()

bat.nocturnal()

#------------------------------------------------------------------------------------------------------------------------------------

