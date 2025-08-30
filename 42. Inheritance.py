# inheritance is when you have a class (i.e., Car), and then you have another class which will inherit the attributes and methods of that car class
# ex: a car can drive, turn, brake. but you might also have a Sports Car class that can do all of those base things, plus some extra features


class Person:
    def move(self):
        print("Moves 4 spaces.")

    def rest(self):
        print("Gains 4 health points.")


# by passing Doctor(Person), we are saying "the Doctor class has ALL of the things the Person class has, and it may also have some more"
class Doctor(Person):
    def heal(self):
        print("Heals all party members for 3 hit points.")


class Fighter(Person):
    def fight(self):
        print(f"{self} causes 10 points of damage.")

    # the fighter also has a move class, but maybe he moves faster than the Person class
    def move(self):
        print("Moves 6 spaces.")


class Wizard(Doctor, Fighter):
    def castSpell(self):
        print("The Wizard has gone invisible.")

    def heal(self):
        print("The Wizard heals 15 hit points to himself.")


character1 = Person()
character2 = Doctor()
character3 = Fighter()
character4 = Wizard()

print("=== PERSON ===")
character1.move()
print("=== DOCTOR ===")
character2.heal()
character2.rest()
print("=== FIGHTER ===")
character3.fight()
character3.move()
print("=== WIZARD ===")
character4.castSpell()
character4.heal()
character4.move()
