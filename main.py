class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color


    def sleep(self):
        print(f"{self.name}He feel a sleep")
        self.endurance += 2


    def eat(self):
        print(f"{self.name}He went to eat")
        self.power += 1


    def hit(self):
        print(f"{self.name}He strikes")
        self.hit -= 5


    def walk(self):
        print(f"{self.name}He walks")
        self.endurance -= 5



    def info(self):
        print(f"The name of the warrior - {self.name}")
        print(f"Warrior's Hair Color - {self.hair_color}")
        print(f"Warrior's Endurance - {self.endurance}")
        print(f"Warrior's Power - {self.power}")


War1 = Warrior("Kratos", 60, 80, "Brown")
print(War1.name)
print(War1.power)
print(War1.endurance)
print(War1.hair_color)
















