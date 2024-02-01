from backend.dbms import Connector as GenericConnector

class Connector(GenericConnector):
    def __init__(self,query):
        self.qu = query
        self.init_connection()
    
    def execute(self):
        return self.cursor.execute(self.qu)
    
    def _insert_items(self,**kwargs):
        for arg in kwargs:

            self.cursor.execute(f"INSERT INTO notes_shop VALUES (1,{arg})")

    
    