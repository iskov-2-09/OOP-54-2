# Родительский класс
class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} готовится к действию.")

    def attack(self):
        print(f"{self.name} атакует врага!")


# Дочерний класс Archer
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision  # значение от 0 до 1

    def attack(self):
        if self.arrows <= 0:
            print(f"{self.name} не может атаковать — нет стрел.")
            return

        self.arrows -= 1
        from random import random
        if random() <= self.precision:
            print(f"{self.name} точно попал в цель! Осталось стрел: {self.arrows}")
        else:
            print(f"{self.name} промахнулся. Осталось стрел: {self.arrows}")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил стрелы. Теперь стрел: {self.arrows}")

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"


# Пример использования
if __name__ == "__main__":
    legolas = Archer("Леголас", 100, 10, 0.8)
    legolas.action()
    legolas.attack()
    legolas.rest()
    print(legolas.status())
