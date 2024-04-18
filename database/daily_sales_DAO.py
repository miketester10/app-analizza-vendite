from database.DB_connect import DBConnect
from model.daily_sale import Daily_sale

class daily_sales_DAO:
    @staticmethod
    def get_anni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT DISTINCT YEAR(Date)
                FROM go_daily_sales;
                """
        cursor.execute(query,)
        result = cursor.fetchall()
        anni = [anno[0] for anno in result]
        
        cursor.close() 
        cnx.close() 
        return anni
    
    @staticmethod
    def get_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        parametri = [('YEAR (DATE)', anno), ('go_products.Product_brand', brand), ('Retailer_code', retailer)]
        query, param_values = _genera_query_dinamica(parametri)
        cursor.execute(query, param_values,)

        result = cursor.fetchall()
        vendite = [Daily_sale(retailer_code=row['Retailer_code'], product_number=row['Product_number'], data=row['Date'], ricavo=float(row['Ricavo'])) for row in result]
        
        cursor.close() 
        cnx.close()
        return vendite

def _genera_query_dinamica(parametri):
    condizioni = []
    param_values = []

    for parametro in parametri:
        if parametro[1]:  # Se il parametro[1] ha un valore, quindi è diverso da None
            condizioni.append(f'{parametro[0]} = %s')
            param_values.append(parametro[1])

    query = '''SELECT Retailer_code, go_daily_sales.Product_number, Date, (Quantity * Unit_sale_price) AS Ricavo 
            FROM go_daily_sales 
            JOIN go_products ON go_daily_sales.Product_number = go_products.Product_number'''
    if condizioni:
        query += ' WHERE '
        query += ' AND '.join(condizioni)
    query += ' ORDER BY Ricavo DESC '

    return query, tuple(param_values) 