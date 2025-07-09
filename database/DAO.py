from database.DB_connect import DBConnect
from model.DailySale import DailySale
from model.Product import Product
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getColors():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT(gp.Product_color) as Color
                    FROM go_products gp 
                    ORDER BY gp.Product_color """
        cursor.execute(query,)
        for row in cursor:
            result.append(row["Color"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(color):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM go_products gp 
                    WHERE Product_color = %s"""
        cursor.execute(query, (color,))
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getWeight(nodo1, nodo2, year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT COUNT(DISTINCT T1.Date) as Weight
                FROM go_daily_sales T1, go_daily_sales T2
                WHERE T1.Date = T2.`Date`
                AND T1.Retailer_code = T2.Retailer_code
                AND T1.Product_number = %s
                AND T2.Product_number = %s
                AND YEAR(T1.Date) = %s"""
        cursor.execute(query, (nodo1.Product_number, nodo2.Product_number, year,))
        for row in cursor:
            result.append(row["Weight"])
        cursor.close()
        conn.close()
        return result