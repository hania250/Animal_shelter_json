import iofile

class AnimalOrganizer:

    def __init__(self, dirpath):
        self.io = iofile.IOAnimals(dirpath)
        self.animals = self.io.load_animals()

    def add_animal(self, name, date, condition, vaccination, notes=''):
        animal = iofile.build_animal(name, date, condition, vaccination, notes)

        self.io.save_animal(animal)

    def find_animal(self, arg, value):
        for animal in self.animals:
            if animal[arg] == value:
                return animal
        raise Exception(" pozycja nie istnieje! ")


    def modify_animal(self, arg, value, set_arg, set_value):
        animal = self.find_animal(arg, value)
        animal[set_arg] = set_value
        self.io.save_animal(animal)

    def get_all_animals(self):
        return self.animals

b = AnimalOrganizer('animals')


#b.add_animal('a', '2011', 'ok', 'nie')
#b.add_animal('c', '2011', 'ok', 'nie')
#print(b.get_all_animals())

b.modify_animal('Name', 'c', 'Vaccination', 'nie')