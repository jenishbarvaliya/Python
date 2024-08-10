class AdultException(Exception):
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) >= 18:
            raise AdultException
        else:
            return self.age

    def display(self):
        try:
            print(f"Minor Age: {self.get_minor_age()}")
        except AdultException:
            print("Age is greater than 18")
        finally:
            print(f"name -> {self.name}")

p1 = Person("Bhavin", 17)
p1.display()

p2 = Person("Dhaval", 23)
p2.display()