import organizer

class Client:
    def __init__(self, animal_dir):
        self.an = organizer.AnimalOrganizer(animal_dir)

    def get_all_animals1(self):
        return self.an.get_all_animals()

    def get_animal_name(self, name):
        return self.an.filter_animal('name', name)

    def get_animal_place(self, place):
        return self.an.filter_animal('place', place)

    def get_animal_vaccination(self, vaccination):
        return self.an.filter_animal('vaccination', vaccination)

    def get_filter_date(self, date1, date2):
        return self.an.filter_animal_date('date', date1, date2)

    def get_modify_date(self, input1, input2):
        self.an.modify_animal('name', input1, 'date', input2)

        #b.modify_animal('name', 'dogg', 'vaccination', 'nie')
        #return self.get_animal_name(input1)

    def add_animal1(self, **kwargs):
        self.an.add_animal(**kwargs)

    def filter_animal(self, arg, value):
        return self.an.filter_animal(arg, value)

c = Client('animals')
#print(c.get_animal_name('a'))
#print(c.get_animal_name(""))
#print(c.get_filter_date('2011', '2011'))
#print(c.get_modify_date('a', '2029'))
c.add_animal1(name='zz', date='2020', condition='nok', vaccination='tak')
print(c.filter_animal('name', 'zz'))