from database.retailers_DAO import retailers_DAO
from database.products_DAO import products_DAO
from database.daily_sales_DAO import daily_sales_DAO

class Model:
    def __init__(self):
        pass

    def get_anni(self):
        anni = daily_sales_DAO.get_anni()
        return anni
    
    def get_brands(self):
        anni = products_DAO.get_brands()
        return anni
    
    def get_retailers(self):
        retailers = retailers_DAO.get_retailers()
        return retailers
    
    def top_vendite(self, anno, brand, retailer):
        vendite = daily_sales_DAO.get_vendite(anno, brand, retailer)
        return vendite[:5] # ritorno solo le prime 5 righe, ovvero le top 5 poichè nella query SQL le ho ordinate per Ricavo in ordine decrescente
    
    def analizza_vendite(self, anno, brand, retailer):
        vendite = daily_sales_DAO.get_vendite(anno, brand, retailer)
        giro_di_affari = sum([vendita.ricavo for vendita in vendite])
        numero_vendite = len(vendite)
        numero_retailer_coinvolti = len(set([vendite.retailer_code for vendite in vendite]))
        numero_prodotti_coinvolti = len(set([vendite.product_number for vendite in vendite]))
        return (giro_di_affari, numero_vendite, numero_retailer_coinvolti, numero_prodotti_coinvolti)
