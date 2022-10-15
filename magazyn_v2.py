import csv
user_choice = -1
sold_items = []

magazyn = [ {'name':'Trimble R2', 'type':'gps', 'quantity':3, 'unit_price':28_000},
    {'name':'Trimble R8', 'type':'gps', 'quantity':5, 'unit_price':14_000},
    {'name':'Leica ATX 1230', 'type':'gps', 'quantity':2, 'unit_price':5_000},
    {'name':'Leica NA520', 'type':'niwelator','quantity':6, 'unit_price':6_500},
]

def show_items():
    """pokazuje stan magazynu"""
    print("Name\t\tType\t\tQuantity\t\tUnit_price")
    for k in magazyn:
        if k['type'] == 'niwelator' or k['type']== 'tachimetr':
            print(k['name'],"\t",k['type'],"\t",str(k['quantity']),"\t\t\t",str(k['unit_price']))
        else:
            print(k['name'],"\t",k['type'],"\t\t",str(k['quantity']),"\t\t\t",str(k['unit_price']))


def add_item():
    """dodaje nowy produkt do magazynu"""
    name = input("Podaj nazwe produktu: ")
    type = input("Podaj typ produktu: ")
    quantity = int(input("Podaj ilość sztuk wprowadzanego produktu: "))
    unit_price = int(input("Podaj cene za jedną sztuke produktu "))

    new_dict = {'name':name, 'type':type, 'quantity':quantity, 'unit_price':unit_price}
    magazyn.append(new_dict)

def sell_item():
    "sprzedaje towar z magazynu"
    global sold_items
    name = input("Podaj nazwe produktu do sprzedaży: ")
    quantity = int(input("Ile sztuk produktu sprzedajesz: "))
    for k in range(len(magazyn)):
        if magazyn[k]['name'] == name:                      
            if magazyn[k]['quantity'] == quantity:
                print("Produkt wyprzedany.")
                sold_items.append(magazyn[k])
                del magazyn[k]
                break
            elif magazyn[k]['quantity'] < quantity:
                print("Ilość sztuk do sprzedania jest większa niż posiadana w magazynie.")
                print("Spróbuj jeszcze raz.")
                break
            else:
                magazyn[k]['quantity'] -= quantity
                new_dict = magazyn[k].copy()
                new_dict['quantity'] = quantity
                sold_items.append(new_dict)
                print("Podana ilośc produktu sprzedana.")
                
    
    return magazyn, sold_items          


print()
print("Witaj w programie M.A.G.A.Z.Y.N.")

while user_choice < 5:
    if user_choice == 1:
        show_items()
    
    if user_choice == 2:
        add_item()

    if user_choice == 3:
        sell_item()

    if user_choice == 4:
        print(sold_items)

    
    print()
    print("MENU:")
    print("1. Wyświetl stan magazynu.")
    print("2. Dodaj produkt do magazynu.")
    print("3. Sprzdaj produkt.")
    print("4. Bilans zysku")

    user_choice = int(input("\nAby poruszać się po menu, podaj cyfrę znajdująca sie przy zadaniu: "))
    print("Możesz wyjsc z programu w każdym momencie, wpisując 'exit'.")

    print()

