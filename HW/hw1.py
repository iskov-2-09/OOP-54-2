class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой age {self.age}, мой city {self.city}")

# Пример использования
person1 = Person("Aibek", 16, "Bishkek")
person1.introduce()

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой age {self.age}, мой city {self.city}")

    def is_adult(self):
        return self.age >= 18

person1 = Person("Алексей", 25, "Москва")
person2 = Person("Ирина", 17, "Казань")
person3 = Person("Миша", 18, "Новосибирск")

print(person1.name, "взрослый?", person1.is_adult())  # True
print(person2.name, "взрослый?", person2.is_adult())  # False
print(person3.name, "взрослый?", person3.is_adult())  # True


