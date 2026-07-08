class Person:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age

    def greet(self):          # method
        return f"Hi, I am {self.name}"

p = Person("Asha", 25)        # object / instance
print(p.greet())