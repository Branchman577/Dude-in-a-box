from dice import d

class Maker():

    race = ""
    def go(self):
        race = self.racechoice()

    def racechoice(self):
        print("It's time to choose a race: \n 1. Humans \n 2. Wood Elves \n 3. Dwarfs \n 4. Halflings")
        try:
            i = input()
            if i == 1:
                return "Human"
            elif i == 2:
                return "Wood Elf"
            elif i == 3:
                return "Dwarf"
            elif i == 4:
                return "Halfling"
            else:
                print("You need to choose either 1 2 3 or 4:")
                return self.racechoice()
        except(NameError):
            print("You need to write in a number.")
            return self.racechoice()
        except(SyntaxError):
            print("You need to write in a number.")
            return self.racechoice()
