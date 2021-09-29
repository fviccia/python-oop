class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark")

    def add(self, x):
        return x + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


myDog = Dog("Tim", 33)
print(myDog.get_age())
myDog.set_age(22)
print(myDog.get_age())
# print(myDog.get_name())
# myDog.bark()
# print(myDog.add(5))
