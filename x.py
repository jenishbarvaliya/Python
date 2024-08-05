class animal():
    def __init__(self,habitate):
        self.habitat = habitate

    def print_habidate(self):
        print(self.habitat)

    def sound(self):
        print("The animal makes a sound")

class dog(animal):
    def __init__(self):
        super().__init__("kennel")

    def sound(self):
        super().sound() #inherited method
        print("The dog barks")

x = dog()
x.print_habidate()
x.sound()
