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


def get_costs():
    """zlicza wartośc produktów w magazynie"""
    cost = [magazyn[k]['quantity'] * magazyn[k]['unit_price'] for k in range(len(magazyn))]
    total_cost = sum(cost)
    print("Wartość produktów w magazynie wynosi:", total_cost,"[PLN]")
    return total_cost

def get_income():
    """zlicza zysk ze sprzedazy towarow"""
    income = [sold_items[k]['quantity'] * sold_items[k]['unit_price'] for k in range(len(sold_items))]
    total_income = sum(income)
    print("Wartość sprzedanych towarów wynosi:", total_income,"[PLN]")
    return total_income
    

def show_revenue():
    """oblicza bilans zyskow/strat w magazynie""" 
    cost = get_costs()
    income = get_income()
    profit = income - cost
    print("Zysk z sprzedanych produktów wynosi:", profit,"[PLN]")
    if profit <= 0:
        print("Nie masz zysku, sprzedaj coś z magazynu.")
   

def export_items_to_csv():
    with open("magazyn.csv", 'w') as csvfile:
        fieldnames = ['name', 'type', 'quantity', 'unit_price']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        for k in magazyn:
            csvwriter.writerow(k)


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
        show_revenue()

    if user_choice == 5:
        export_items_to_csv()

    
    print()
    print("MENU:")
    print("1. Wyświetl stan magazynu.")
    print("2. Dodaj produkt do magazynu.")
    print("3. Sprzdaj produkt.")
    print("4. Bilans zysku")
    print("5. Zapis danych")
    print("6. Wczytanie danych")


    user_choice = int(input("\nAby poruszać się po menu, podaj cyfrę znajdująca sie przy zadaniu: "))
    print("Możesz wyjsc z programu w każdym momencie, wpisując 'exit'.")

    print()

