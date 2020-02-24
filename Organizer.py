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
        print(filenames)
        animals = []
        for filename in filenames:
            d = self.load_animal(filename)
            animals.append(d)
        return animals

    def build_animal(self, name,
                     date,
                     condition,
                     vaccination,
                     notes=''):
        d = {
            "Name": name,
            "Date": date,
            "Condition": condition,
            "Vaccination": vaccination,
            "Notes": notes
        }
        return d

    def save_animal(self, animal):
        title = animal['Name']
        title = title.lower()
        title = title.replace(' ', '_')
        print(title)

        with open(self.get_filename(title) + '.json', 'w') as f:
            json.dump(animal, f)

a = IOAnimals('animals')
item = a.build_animal('dog', '2019', 'ok', 'nie')
a.save_animal(item)

