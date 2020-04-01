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
        condition1 = input('Podaj stan ')
        vaccination1 = input('Szczepienie')
        d.add_animal1(name=name1, date=date1, condition=condition1, vaccination=vaccination1)
    elif text == 'lista':
        e = d.get_all_animals1()
        l1 = []
        for item in e:
            print(item['name'])
            l1.append(item['name'])
        print(l1)
        #for item in e:
          #  print_1(item)
    elif text == 'modyfikuj date':
        r = input('podaj zwierza')
        e = input('podaj nowa date')
        d.get_modify_date(r, e)
    elif text == 'znajdz zwierza':
        r = input('Podaj argument')
        e = input('Podaj wartosc argumentu')
        print(d.filter_animal(r, e))
    elif text == 'usun zwierza':
        item = input('podaj imie zwierza ')
        d.delete_animal(item)
        d.get_all_animals1()
    elif text == 'zaladuj':
        d.get_all_animals1()
        continue
    elif text == 'zakoncz':
        d.get_all_animals1()
        break