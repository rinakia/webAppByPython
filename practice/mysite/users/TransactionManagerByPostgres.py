""" ---------------------------------
# 
#  class
# 
#   ----------------------------------
""" 
import psycopg2
import os
class TransactionManagerByPostgres:    

    # dsn = os.environ.get('DATABASE_URL')
    # DATABASE_URL = postgresql://{username}:{password}@{hostname}:{port}/{database}

    def __init__(self):
        self.dsn ="dbname=sample user=sample1"
        self.conn : psycopg2.extensions.connection
        self.cur  : psycopg2.extensions.connection.cursor
            
    # def __del__(self):
        # デストラクタ
        # print("さようなら")

    # print
    def samplePrint(self):
        print(self.dsn)

    def setConnection(self):
        try:
            # postgres
            self.conn = psycopg2.connect(self.dsn)
        except OperationalError as e:
            print("OperationalError")
            raise e
    
    def getConnection(self) -> psycopg2.extensions.connection:
        try:
            """
            self.conn = psycopg2.connect(dsn)
            return self.conn
            """
            return psycopg2.connect(self.dsn)
        except OperationalError as e:
            print("OperationalError")
            raise e
            
    def closeConnection(self):
        self.conn.close()


    def setCursor(self):
        try:
            self.cur = self.conn.cursor()
        except InterfaceError as e:
            print("InterfaceError")
            print("connectionが見つかってないはず、")
            raise e
            
    def getCursor(self) -> psycopg2.extensions.connection.cursor:
        try:
            self.cur = self.conn.cursor()
            return self.cur
        except InterfaceError as e:
            print("InterfaceError")
            print("connectionが見つかってないはず、")
            raise e
            
    def closeCursor(self):
        self.conn.close()

