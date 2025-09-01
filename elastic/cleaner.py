from dal.connection import Connection
import os

class Cleaner:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.idx_name = os.getenv("IDX_NAME",'tweets')

    def delete(self,id):
        if self.es.indices.exists(index=self.idx_name):
            self.es.indices.delete(index=self.idx_name,id=id)
            print(f'ID: {id} deleted')