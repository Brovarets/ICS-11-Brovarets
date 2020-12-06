from data_service import get_dovidnik, get_prices

zmina = {
    'name market'                          : "",     # найменування ринку
    'name product'                         : "",     # найменування товара
    'Unit'                                 : "",     # одиниця виміру
    'price level in 2007'                  : 0,      # зміна рівня цін 2007
    'price level in 2008 in UAH'           : 0,      # зміна рівня цін 2008 у грн
    'price level in 2008 in % to 2007'     : 0,      # зміна рівня цін 2008 у % до 2007
    'price level in 2011 in UAH'           : 0,      # зміна рівня цін 2011 у грн
    'price level in 2011 in % to 2008'     : 0,      # зміна рівня цін 2011 у % до 2008
    'price level of 2017 in UAH'           : 0,      # зміна рівня цін 2017 у грн
    'price level of 2017 in % to 2011'     : 0       # зміна рівня цін 2017 у % до 2011
}



def create_zmina():
    dovidniks = get_dovidnik()
    price = get_prices()

    def get_dovidnik_name(dovidnik_code):
        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]
        return "*** назва не знайдена"

    def get_dovidnik_discount(dovidnik_code):
        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[2]
        return "*** назва не знайдена"
    zmina_list = []
    


    for prices in price:
        zmina_copy = zmina.copy()  

        zmina_copy['name market']                       = get_dovidnik_name market(prices[0])
        zmina_copy['name product']                      = prices[3].rstrip()
        zmina_copy['Unit']                              = prices[1]
        zmina_copy['price level in 2007']               = float(get_dovidnik_price level in 2007(prices[0]))
        zmina_copy['price level in 2008 in UAH']        = int(zmina_copy['price level in 2008 in UAH']) * int(zmina_copy['price level in 2007'] * 10) / 10
        zmina_copy['price level in 2008 in % to 2007']  = int(zmina_copy['price level in 2008 in % to 2007']) * int(zmina_copy['price level in 2007'] * 10) / 10
        zmina_copy['price level in 2011 in UAH']        = int(zmina_copy['price level in 2011 in UAH']) * int(zmina_copy['price level in 2007'] * 10) / 10
        zmina_copy['price level in 2011 in % to 2008']  = int(zmina_copy['price level in 2011 in % to 2008']) * int(zmina_copy['price level in 2007'] * 10) / 10
        zmina_copy['price level of 2017 in UAH']        = int(zmina_copy['price level of 2017 in UAH']) * int(zmina_copy['price level in 2007'] * 10) / 10
        zmina_copy['price level of 2017 in % to 2011']  = int(zmina_copy['price level of 2017 in % to 2011']) * int(zmina_copy['price level in 2007'] * 10) / 10
        zmina_list.append(zmina_copy)
    return zmina_list
#result = create_zmina()

#for line in  result:
#    print(line)