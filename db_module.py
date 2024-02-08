# Module Imports
import mysql.connector
import os
from mysql.connector import Error
dbpassword = os.getenv('DBPASSWORD')

class InsertData:

    def __init__(self):
        self.host = "localhost"
        self.port = 3307
        self.user = "root"
        self.password = dbpassword



    def connect_db(self):
        conn = mysql.connector.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database ='new_db'
        )
        return conn
        #return "Successfully connected to the database"

    def query_db(self):
        condb = self.connect_db()
        cursor = condb.cursor()
        query_data_table = """SELECT * FROM dailydb"""
        cursor.execute(query_data_table)
        current_db_data = cursor.fetchall()
        print(f"the current data in the db are: {current_db_data}")

    def insert_db(self, date, username, title, dayplan):
        condb = self.connect_db()
        cursor = condb.cursor()
        insert_data_table = """INSERT INTO dailydb(date, name, title, dayplan)
                            VALUES (%s, %s, %s, %s)"""
        data_tuple = (date, username, title, dayplan)
        cursor.execute(insert_data_table, data_tuple)
        condb.commit()
        return "Record inserted successfully"

# user1 = InsertData()
# print(user1.password)
# result = user1.query_db()
# user2 = InsertData()
# result = user2.insert_db("feb 4th", "lk", "az", "az104")
# print(result)

