import json
import os

def load_animal(filename):
    with open('animals/' + filename, 'r') as f:
        d = json.load(f)
        return d

def load_animals():
    filenames = os.listdir('animals')
    print(filenames)
    animals = []
    for filename in filenames:
        d = load_animal(filename)
        animals.append(d)
    return animals

def build_animal(name,
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

def save_animal(animal):
    title = animal['Name']
    title = title.lower()
    title = title.replace(' ', '_')
    print(title)

    with open('animals/' + title + '.json', 'w') as f:
        json.dump(animal, f)

#print(load_animals())
#for animal in load_animals():
#   print(animal)

a = build_animal('ww we','20.01.2020', 'ok', 'tak')
save_animal(a)