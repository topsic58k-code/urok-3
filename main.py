class Student:
    def __init__(self, name, age, height, number):
        self.age = age
        self.height = height
        self.number = number
        self.name = name

    def grow(self, height = 1):
        self.height += height


anton = Student(name="Anton", age=12, height=166, number=38054345345)

print("Name - ", anton.name)
print("Age - ", anton.age)
print("Height - ", anton.height)
print("Phone number - ", anton.number)

anton.grow(height=5)
print(anton.height)