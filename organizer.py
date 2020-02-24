import iofile

class AnimalOrganizer:

    def __init__(self, dirpath):
        self.io = iofile.IOAnimals(dirpath)
        self.animals = self.io.load_animals()

    def add_animal(self, name, date, condition, vaccination, notes=''):
        animal = iofile.build_animal(name, date, condition, vaccination, notes)

        self.io.save_animal(animal)

    def modify_animal(self):
        pass

    def get_all_animals(self):
        return self.animals

b = AnimalOrganizer('animals')
print(b.get_all_animals())