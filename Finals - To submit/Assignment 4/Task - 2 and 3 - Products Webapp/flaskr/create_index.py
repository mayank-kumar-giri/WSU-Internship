from elasticsearch import Elasticsearch

def create_index(index):
    ES_HOST = {"host": "localhost", "port": 9200}
    es = Elasticsearch(hosts=[ES_HOST])
    request_body = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
    }
    if es.indices.exists(index):
        print("deleting '%s' index..." % (index))
        res = es.indices.delete(index=index)
        print(" response: '%s'" % (res))
    print("Creating",index,"index...")
    es.indices.create(index=index, body=request_body)

if __name__ == "__main__":
    create_index("catalogue")