import client

def print_1(animal):
    name2 = animal['name']
    print(name2)

def print_2(animals):
    for animal in animals:
        print_1(animal)

d = client.Client('animals')
#d.add_animal1(name='zwwww', date='2010', condition='ok', vaccination='nie')



while True:
    text = input('Co chcesz zrobić? ')

    if text == 'dodaj':
        name1 = input("Podaj imię ")
        date1 = input('Podaj datę ')
        condition1 =input('Podaj stan ')
        vaccination1 =input('Szczepienie')
        d.add_animal1(name=name1, date=date1, condition=condition1, vaccination=vaccination1)
    elif text == 'lista':
        e = (d.get_all_animals1())
        l1 = []
        for item in e:
            print(item['name'])
            l1.append(item['name'])
        print(l1)
        #for item in e:
          #  print_1(item)