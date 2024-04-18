from database.DB_connect import DBConnect
from model.retailer import Retailer

class retailers_DAO:
    @staticmethod
    def get_retailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM go_retailers ;
                """
        cursor.execute(query,)
        result = cursor.fetchall()
        retailers = [Retailer(retailer_code=retailer['Retailer_code'], retailer_name=retailer['Retailer_name'], type=retailer['Type'], country=retailer['Country']) for retailer in result]

        cursor.close() 
        cnx.close() 
        return retailers
      