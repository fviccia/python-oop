class Math:

    # For organizational concerns sometimes you want to define functions inside classes
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    # Is not necessary to pass any attributes to the method
    @staticmethod
    def pr():
        print("Run")


print(Math.add5(5))
print(Math.add10(5))
Math.pr()
