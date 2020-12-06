""" розрахунок заявок на товари по магазину
"""

from data_service import get_orders, get_clients

# словник в якому будуть накопичуватись результати розрахунків
zajavka = {
    'oborud' : "",     # назва устаткування
    'client' : "",     # назва клієнта
    'zakaz'  : "",     # номер заказа
    'kol'    : 0,      # кількість товару
    'price'  : 0.0,    # ціна
    'total'  : 0.0     # сума
}

def create_zajavka():
    """формування списку заявок по магазину на основі вхідних файлів
    """
    orders = get_orders()
    clients = get_clients()

    def get_client_name(client_code):
        """повертає назву клієнта по його коду

        Args:
            client_code : код клієнта 

        Returns:
            client_name: назив клієнта
        """

        for client in clients:
            if client[0] == client_code:
                return client[1]

            return "*** назва не знайдена"           

    # список заявк по магаину, що формується
    zajavka_list = []

    # обробляємо послідовно кожний рядок 'orders`
    for order in orders:
        
        # підготувати робочий словник для рядка `order`
        zajavka_copy = zajavka.copy()

        # заповнити робочий словник значеннями з `order`
        zajavka_copy['oborud'] = order[2]
        zajavka_copy['zakaz']  = order[1]
        zajavka_copy['kol']    = order[3]
        zajavka_copy['price']  = order[4]
        zajavka_copy['total']  = zajavka_copy['kol'] * zajavka_copy['price']
        zajavka_copy['client'] = get_client_name(order[0])

        zajavka_list.append(zajavka_copy)

    return zajavka_list


result = create_zajavka()

for line in  result:
    print(line)