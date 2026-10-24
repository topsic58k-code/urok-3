class GermanShepherd:

    def __init__(self, name, age, size):
        self.name = name  # Ім'я собаки
        self.age = age  # Вік у роках
        self.size = size  # Розмір (наприклад: "великий", "середній")

    def show_info(self):
        print(f"Собака: {self.name}")
        print(f"Вік: {self.age} років")
        print(f"Розмір: {self.size}")


# Створюємо новий об'єкт вівчарки
dog1 = GermanShepherd(name="швайне", age=3, size="великий")

# Виводимо інформацію про собаку
dog1.show_info()