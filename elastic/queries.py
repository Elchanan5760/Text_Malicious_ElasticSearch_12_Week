from dal.connection import Connection
import os

class Queries:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.idx_name = os.getenv("IDX_NAME",'tweets')

    def quarry(self,query):
        if self.es.indices.exists(index=self.idx_name):
            self.es.indices.delete(index=self.idx_name,body={"query": query})
            print("The query succeed")