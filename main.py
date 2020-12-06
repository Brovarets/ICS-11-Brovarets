import os
from process_data import create_zmina
from data_service import show_dovidnik, show_prices, get_prices, get_dovidnik  
import codecs

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~~~~~~ ОБРОБКА ЗМІНИ ЦІНИ НА ПОТОЧНИЙ РІК ~~~~~~~~~~~~~~~~~~~~~ 
1 - вивід доходу на екран
2 - запис доходу в файл
3 - вивід середньої ціни на основні продовольчих товарів
4 - вивід довідника товарів
0 - завершити роботу
_________________________________
"""

TITLE = "ЗМІНИ ЦІНИ НА ПОТОЧНИЙ РІК"
HEADER = \
'''
===================================================================================================================
|  Найменування  |  Найменування  |  Одиниця  |                     Зміна рівня цін по рокам                      |
|     ринку      |     товара     |  виміру   |===================================================================|
|                |                |           |      2007      |      2008      |      2011      |      2017      | 
|                |                |           |                |================|================|================|
|                |                |           |                |  грн.  |у % до |  грн.  |у % до |  грн.  |у % до |
|                |                |           |                |        | 2007  |        | 2008  |        | 2011  |
===================================================================================================================
'''
FOOTER = \
'''
=====================================================================================================
'''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"


def show_zmina(zmina_list):
    print(f'\n\n{TITLE:^103}')
    print(HEADER)
    
    for zmina in zmina_list:
        print(f"{zmina['name market']:17}", 
              f"{zmina['name product']:^7}",
              f"{zmina['Unit']:^10}",
              f"{zmina['price level in 2007']:^20}",
              f"{zmina['price level in 2008 in UAH']:^11.1f}",
              f"{zmina['price level in 2008 in % to 2007']:^12.1f}",
              f"{zmina['price level in 2011 in UAH']:^20.1f}"
              f"{zmina['price level in 2011 in % to 2008']:^25.1f}"
              f"{zmina['price level of 2017 in UAH']:^17.1f}"
              f"{zmina['price level of 2017 in % to 2011']:^21.1f}"
              )
    print(FOOTER)  
    
def write_file(zmina_list):
    with codecs.open('./data/zmina.txt', "w",  encoding='utf-8') as zmina_file:
        for zmina in zmina_list:
            line = \
                f"{(zmina['name market']) + ';':20}"                   + \
                f"{(zmina['name product']) + ';':8}"                    + \
                f"{(zmina['Unit']) + ';':8}"         + \
                f"{(zmina['price level in 2007']) + ';':8}"   + \
                f"{(str(zmina['price level in 2008 in UAH'])) + ';':7}"           + \
                f"{(str(zmina['price level in 2008 in % to 2007'])) + ';':11}"        + \
                f"{(str(zmina['price level in 2011 in UAH'])) + ';':11}"        + \
                f"{(str(zmina['price level in 2011 in % to 2008'])) + ';':9}"        + \
                f"{(str(zmina['price level of 2017 in UAH'])) + ';':9}"        + \
                f"{(str(zmina['price level of 2017 in % to 2011'])) + ';':5}" + '\n'
            
            zmina_file.write(line)
    
    print("Файл успішно сформовано ...")
            


while True: 
    os.system('clear')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди: ')
    
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)

    elif command_number == '1':
        zmina_list = create_zmina()
        show_zmina(zmina_list)  
        input(STOP_MESSAGE)  

    elif command_number == '2':
        zmina_list = create_zmina()
        write_file(zmina_list)
        input(STOP_MESSAGE)

    elif command_number == '3':
        pricess = get_prices()
        show_prices(pricess)
        input(STOP_MESSAGE)

    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidnik(dovidniks)
        input(STOP_MESSAGE)