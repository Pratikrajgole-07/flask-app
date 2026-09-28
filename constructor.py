class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create object
s1 = Student("Pratik", 20)

# Display data
s1.display()