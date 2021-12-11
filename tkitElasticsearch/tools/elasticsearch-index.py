#如何获取此群集中所有索引的列表？

#使用通配符。适用于elasticsearch-py。
from elasticsearch import Elasticsearch
es = Elasticsearch('127.0.0.1:9200')
for index in es.indices.get('*'):
  print(index)
