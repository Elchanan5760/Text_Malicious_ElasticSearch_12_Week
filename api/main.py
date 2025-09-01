from dal.read_csv import Load_CSV
from elastic.mapping import Mapping
from elastic.loader import Loading
from elasticsearch import Elasticsearch

if __name__=='__main__':
    es = Elasticsearch("http://localhost:9200")

    map = Mapping()
    load = Loading()
    actions = []
    print('mapping\n',map.map_idx("tweets"))
    print('loading\n',load.load_es(Load_CSV.read_csv()[:2]),'\n')
    res = es.search(index='tweets', query={"match_all": {}})
    print('search',res["hits"]["hits"])
