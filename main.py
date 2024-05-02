class Warrior():
    def __init__(self, name, power, endurance, hair_color, info):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
        self.info = info

    def sleep(self):
        print(f"{self.name}"He feel a sleep")
        self.endurance += 2


    def eat(self):
        print(f"{self.name}"He sat down to eat")
        self.power += 1


    def hit(self):
        print(f"{self.name}"Ye strikes")
        self.hit -= 5


    def walk(self):
        print(f"{self.name}"He walks")
        self.endurance -= 5



    def info(self):
        print(f"The name of the warrior - {self.name}")
        print(f"Warrior's Hair Color - {self.hair_color}")
        print(f"Warrior's Endurance - {self.endurance}")
        print(f"Warrior's Power - {self.power}")














