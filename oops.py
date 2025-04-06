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

#print(aniket.salary)  # Accessing the class attribute using the object

aniket.travel("Pune") # Calling the method using the object

print(type(aniket))  # Checking the type of the object





