class School:

    def wear_uniform(self):
        return "В школе все должны носить форму"

class University:

    def wear_uniform(self):
        return "Можно носить любую одежду, если ты студент"

s = School()
u = University()

s.wear_uniform()
u.wear_uniform()