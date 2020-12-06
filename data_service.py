def get_dovidnik():
    with open("./data/dovidnik.txt", encoding='utf-8') as dovidnik_file: # encoding='utf-8' - нужно чтобы коректно отображать руские буквы, а не символы непонятные
        from_dovidnik = dovidnik_file.readlines()

    dovidnik_list = [] 

    for line in from_dovidnik:
        line_list = line.split(';')
        dovidnik_list.append(line_list)
      
      
    return dovidnik_list

def get_prices():
    with open("./data/prices.txt", encoding='utf-8') as prices_file:
        from_prices = prices_file.readlines()

    prices_list = [] 

    for line in from_prices:
        line_list = line.split(';')
        prices_list.append(line_list)
      
    return prices_list

def show_dovidnik(dovidnik):
    dovidnik_code_from = input("З якого коду товарів?")
    dovidnik_code_to = input("По який код товарів?")

    kol_lines = 0

    for cod in dovidnik:
        if dovidnik_code_from <= cod[0] <= dovidnik_code_to:
            print("Код: {:8} Назва:{:20} Одиниця виміру:{:4}".format(cod[0], cod[1], cod[2].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(dovidnik_code_from, dovidnik_code_to))

def show_prices(prices):
    prices_code_from = input("З якого коду товарів?")
    prices_code_to = input("По який код товарів?")

    kol_lines = 0

    for cod in prices:
        if prices_code_from <= cod[0] <= prices_code_to:
            print("Код:{:7} Ціна:{:8} Найменування ринку:{:6}".format(cod[0], cod[1], cod[2], cod[3].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(prices_code_from, prices_code_to))



# what_show = int(input("Показати: 1 - довідник; 2 - ціна? (1/2)"))
# if what_show == 1:
#dovidnik = get_dovidnik()
#show_dovidnik(dovidnik)   
# elif what_show == 2:
#prices = get_prices()
#show_prices(prices)
# else:
#    print("Введіть '1' або '2'!")  