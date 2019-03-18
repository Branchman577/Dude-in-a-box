from dice import d

class Maker():
    race = ""
    def go(self):
        race = self.racechoice()

    def racechoice(self):
        i = d(1,4)
        if i[0] == 1:
            return "Human"
        elif i[0] == 2:
            return "Wood Elf"
        elif i[0] == 3:
            return "Dwarf"
        elif i[0] == 4:
            return "Halfling"
