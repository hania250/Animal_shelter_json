import json
import os

class IOAnimals:

    def __init__(self, dirname):
        self.dirname = dirname

    def get_filename(self, animal):
        return self.dirname + '/' + animal

    def load_animal(self, filename):
        with open(self.get_filename(filename), 'r') as f:
            d = json.load(f)
            return d

    def load_animals(self):
        filenames = os.listdir(self.dirname + '/')
        #print(filenames)
        animals = []
        for filename in filenames:
            d = self.load_animal(filename)
            animals.append(d)
        return animals


    def save_animal(self, animal):
        title = animal['name']
        title = title.lower()
        title = title.replace(' ', '_')
        #print(title)
        with open(self.get_filename(title) + '.json', 'w') as f:
            json.dump(animal, f)

def build_animal(**kwargs):
    required = ['name', 'date', 'condition', 'vaccination']
    optional = [('notes', ""), ('place', "")]

    for arg in required:
        if arg not in kwargs:
            raise Exception(arg + " nie istnieje w obiekcie")

    for arg, default in optional:
        if arg not in kwargs:
            kwargs[arg] = default

    return kwargs

if __name__=='__main__':
    a = IOAnimals('animals')
    item = build_animal(name='dogg',date='2019', condition='ok', vaccination='nie')
    a.save_animal(item)
    #print(a.load_animals())
#b = build_animal(name='abc', vaccination='nie', date='2019', condition='ok')
#a.save_animal(b)