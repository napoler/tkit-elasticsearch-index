from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch('127.0.0.1:9200')

index_v = "tkit-index-test2"

doc_type_v = "*"

# query = {"query": {"match": {"_id": "d1e2b7322bc6c25327d3083e1f8de276"}}}
query = {"query": {"match": {"_id": "d1e2b7322bc6c253"}}}
# scanResp = helpers.scan(client=es, query=query, scroll="10m", index=index_v, doc_type=doc_type_v, timeout="10m")
scanResp = helpers.scan(client=es, query=query, scroll="10m", index=index_v, timeout="10m")
for resp in scanResp:
    qid = resp['_id']
    print(qid)
    print(resp)
