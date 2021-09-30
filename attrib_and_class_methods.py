class Person:
    # Class Attribute, not specific to any instance.
    # Usefull for defining constants for example
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Call the class method
        Person.add_person()

    # Class Methods acts in the class itself and not only in behalf of a particular isntance
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Jill")

# Person.number_of_people = 8  # This changes directly the class variable
# print(p2.number_of_people)
print(Person.number_of_people_())
