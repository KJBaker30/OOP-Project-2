class Person:
    def __init__(self, noun):
        self.age = 20
        self.name = noun
        print('heyhey')

person1 = Person('Keira')

print(person1.name)