class Human:

    def eat_spaghetti(self):
        print("Я могу есть спагетти")

class Robot:

    def drink_oil(self):
        print("Я могу  потреблять машинное масло")

class Cyborg(Human, Robot):
     pass

c = Cyborg()
c.drink_oil()
c.eat_spaghetti()