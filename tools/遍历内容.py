from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch('127.0.0.1:9200')

index_v = "tkit-index-test2"
index_v = "chinese_sents_next"
doc_type_v = "*"

query = {"query": {"match_all": {}}}
# query = {"query": {"match_all": {"_source": {"body": {"content": "鸡新"}}}}}

# query = {"query": {"match_all": {"_source": ["content"]}}}

#
# query = {
#     'query': "鸡新",
#     '_source': ['content']
# }
# scanResp = helpers.scan(client=es, query=query, scroll="10m", index=index_v, doc_type=doc_type_v, timeout="10m")
scanResp = helpers.scan(client=es, query=query, scroll="10m", index=index_v, timeout="10m")
for resp in scanResp:
    qid = resp['_id']
    print(qid)
    print(resp)
