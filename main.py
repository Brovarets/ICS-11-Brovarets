"""головний модуль додатку
виводить розрахункову таблицю, зберігає розрахунок у файлі,
показує на екрані первинні дані
"""
import os
from process_data import create_zajavka_list
from data_service import show_clients, show_orders, get_orders, get_clients

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~~~~~~~~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід довідника клієнтів
0 - завершити роботу
---------------------------------
"""

TITLE = 'ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ ПО МАГАЗИНУ'

HEADER = \
"""
=====================================================================================
|   Устаткування     |   Клієнт      | Номер заказа| Кількість |  Ціна   | Сума     |
=====================================================================================
"""

STOP_MESSAGE = "Для продовження натисніть <Enter>"

FOOTER = \
"""
=====================================================================================

"""
def show_zajavka(zajavka_list):
    """вивод на екран розрахункової таблиці

    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n\n{TITLE:^86}")
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['oborud_name']:22}", 
              f"{zajavka['client_name']:17}",
              f"{zajavka['order_number']:^10}",
              f"{zajavka['kol']:8}",
              f"{zajavka['price']:>11.2f}",
              f"{zajavka['total']:>11.2f}"
              )
     
    print(FOOTER)   

def write_file(zajavka_list):
    """запис списку заявок в файл

    Args:
        zajavka_list ([type]): список заявок
    """
    with open('./data/zajavka.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line = \
                zajavka['oborud_name'] + ';'      + \
                zajavka['client_name'] + ';'      + \
                str(zajavka['kol']) + ';'         + \
                str(zajavka['price']) + ';'       + \
                str(zajavka['total']) + ';' + '\n'
            
            zajavka_file.write(line)
    
    print("Файл успішно сформовано ...")
            

while True:
    os.system('clear')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди: ')
    
    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        zajavka_list = create_zajavka_list()
        show_zajavka(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '2':
        zajavka_list = create_zajavka_list()
        write_file(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        orders = get_orders()
        show_orders(orders)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        clients = get_clients()
        show_clients(clients)
        input(STOP_MESSAGE)
        

        
    