from dal.connection import Connection

class Mapping:
    def __init__(self):
        self.es = Connection.get_es_client()

    def map_idx(self,idx_name):
        mapping =  {
                    "mappings": {
                        "properties": {
                            "id": {"type": "keyword"},
                            'date': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                            'antisemitic': {"type": "boolean"},
                            "text": {"type": "text"}
                        }
                    }
                }
        if not self.es.indices.exists(index=idx_name):
            res = self.es.index(index=idx_name, body=mapping)
            return res
