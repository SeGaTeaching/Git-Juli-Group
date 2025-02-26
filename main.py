class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name

heike = Person("Heike", 31)
print(heike)
erich = Person("Erich", 23)
print(erich)