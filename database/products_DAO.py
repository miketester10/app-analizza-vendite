from database.DB_connect import DBConnect

class products_DAO:
    @staticmethod
    def get_brands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT DISTINCT Product_brand 
                FROM go_products;
                """
        cursor.execute(query,)
        result = cursor.fetchall()
        prodotti = [prodotto[0] for prodotto in result]
        
        cursor.close() 
        cnx.close() 
        return prodotti