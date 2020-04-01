import iofile
import os

class AnimalOrganizer:

    def __init__(self, dirpath):
        self.io = iofile.IOAnimals(dirpath)
        self.animals = self.io.load_animals()

    def add_animal(self, **kwargs):
        animal = iofile.build_animal(**kwargs)
        self.io.save_animal(animal)

    def filter_animal(self, arg, value):
        l = []
        for animal in self.animals:
            if animal[arg] == value:
                l.append(animal)
        return l

    def filter_animal_date(self, arg, lower_date, upper_date):
        l = []
        for animal in self.animals:
            if lower_date <= animal[arg] <= upper_date:
                l.append(animal)
        return l


    def find_animal(self, arg, value):
        l = self.filter_animal(arg, value)
        if len(l) != 1:
            raise Exception(" nie znaleziono tylko jednej pozycji!")
        return l[0]

    def modify_animal(self, arg, value, set_arg, set_value):
        animal = self.find_animal(arg, value)
        animal[set_arg] = set_value
        self.io.save_animal(animal)

    def get_all_animals(self):
        return self.animals

    def delete(self, item):
        d = self.io.get_filename(item) + '.json'
        if os.path.exists(d):
            os.remove(d)
        else:
            print("The file does not exist")
        self.animals

b = AnimalOrganizer('animals')

#b.add_animal(name='acddx', date='2011', condition='ok', vaccination='nie')
#b.delete('dogg')

#b.add_animal('c', '2011', 'ok', 'nie')
#print(b.get_all_animals())

#b.modify_animal('name', 'dogg', 'vaccination', 'nie')
#print(b.filter_animal('name', 'a'))
#print(b.filter_animal_date('date', '2011', '2019'))
#print(b.find_animal('date', '2011'))