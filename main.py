class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name

erich = Person("Erich", 23)
print(erich)

