class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
p = Person('Alex', 'Galkin', 45)

print(p.firstname, p.lastname, p.age)