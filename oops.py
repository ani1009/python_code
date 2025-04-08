# Initiating a class:

class employee:
    # Class attributes

    def __init__(self):
        print("Started Executing attributes/data")

        self.id = 1009
        self.age = 26
        self.salary = 100000
        self.designation = "AI Engineer"

        print("Finished Executing attributes/data")

    def travel(self, destination):
        print("This travel Method is called manually")

        print(f"Employee is travelling to {destination}")


# Creating an object of the class:
aniket = employee()
ram = employee()

#print(aniket.salary)  # Accessing the class attribute using the object

aniket.travel("Pune") # Calling the method using the object

print(type(aniket))  # Checking the type of the object

print(id(aniket))  # Checking the memory address of the object
print(id(ram))  # Checking the memory address of the object

print(aniket.__class__)  # Checking the class of the object
print(aniket.__dict__)  # Checking the attributes of the object




