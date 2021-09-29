# Without inheritance


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Bark")


# With inheritance


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")


class Cat(Pet):  # Pass another class to inherit from
    def speak(self):  # This method overwrites the general one
        print("Meow")


class Dog(Pet):
    # I can overwrite initialization to add some different atributes
    def __init__(self, name, age, color):
        # Call the parent class to initialize the attributes
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Bark")


p = Pet("Tim", 22)
p.show()
c = Cat("Capu", 8)
c.show()
c.speak()
d = Dog("Jill", 13, "Brown")
d.show()
d.speak()
print(d.color)
