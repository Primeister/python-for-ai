class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")


person1 = person("Alice", 24)

print(person1.name)
person1.greet()