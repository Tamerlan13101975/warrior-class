class Warrior():
    def __init__(self, name, power, endurance, hair_color, info):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
        self.info = info

    def sleep(self):
        print(f"{self.name}"Лег спать")
        self.endurance += 2


    def eat(self):
        print(f"{self.name}"Сел кушать")
        self.power += 1


    def hit(self):
        print(f"{self.name}"Наносит удар")
        self.hit -= 5


    def walk(self):
        print(f"{self.name}"Идет куда-то")
        self.endurance -= 5



    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цвет волос воина - {self.hair_color}")
        print(f"Выносливость воина - {self.endurance}")
        print(f"Сила воина - {self.power}")














