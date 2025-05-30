class Student:
    def __init__(self, name, grade=0):
        self.__name = name
        self.__grade = 0
        self.set_grade(grade)

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Ошибка: оценка должна быть от 0 до 100")

    def get_grade(self):
        return self.__grade

    def get_info(self):
        return f"Имя: {self.__name}, Оценка: {self.__grade}"


# Пример
student = Student("Иван", 85)
print(student.get_info())  # Имя: Иван, Оценка: 85

student.set_grade(105)     # Ошибка: оценка должна быть от 0 до 100

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Примеры
circle = Circle(5)
square = Square(4)

print("Площадь круга:", circle.area())   # Площадь круга: 78.5
print("Площадь квадрата:", square.area())  # Площадь квадрата: 16
