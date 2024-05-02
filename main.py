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
        self.endurance -= 5


    def walk(self):
        print(f"{self.name}He walks")
        self.endurance -= 5



    def info(self):
        print(f"The name of the warrior - {self.name}")
        print(f"Warrior's Hair Color - {self.hair_color}")
        print(f"Warrior's Endurance - {self.endurance}")
        print(f"Warrior's Power - {self.power}")


War1 = Warrior("Kratos", 60, 80, "Brown")
War2 = Warrior("Sander", 75, 60, "Gray-haired")
print(War1.name)
print(War1.power)
print(War1.endurance)
print(War1.hair_color)
print(War2.name)
print(War2.power)
print(War2.endurance)
print(War2.hair_color)


print(War1.endurance)
print(War1.power)
War1.sleep()
War1.eat()
War1.hit()
print(War1.endurance)
print(War1.power)

print(War2.endurance)
print(War2.power)
War2.walk()
War2.sleep()
War2.sleep()
print(War2.endurance)
print(War2.power)


War1.sleep()
War1.eat()
War1.hit()
War1.walk()
War1.info()

War2.sleep()
War2.eat()
War2.hit()
War2.walk()
War2.info()











