import mysql.connector as mysql
from backend.settings import MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE_NOTES_SHOP

class Connector(object):
    def __init__(self,database) -> None:
        self.username = MYSQL_USERNAME
        self.password = MYSQL_PASSWORD
        self.host = MYSQL_HOST
        self.db = database
        self.connection = mysql.connect(user=self.username, password=self.password, host=self.host, database=self.db)
        self.cursor = self.connection.cursor()
    
    def init_connection(self):
        return self.connection
    
    def execute(self,query):
        return self.cursor.execute(query)

