from dal.connection import Connection
from elasticsearch.helpers import bulk
import os

class Loading:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME",'tweets')
    def load_es(self,data):
         actions = [
            {
                "_index": self.IDX_NAME,
                "_id": str(row['TweetID']),
                "_source": {
                    "id": str(row['TweetID']),
                    "date": row['CreateDate'],
                    "antisemitic": row['Antisemitic'],
                    "text": row['text']
                }
            }
            for row in data
        ]
         bulk(self.es,actions)
         return actions