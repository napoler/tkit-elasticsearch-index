# -*- coding: utf-8 -*-
"""
作者：　terrychan
Blog: https://terrychan.org
# 说明：
for es index

#如何获取此群集中所有索引的列表？

#使用通配符。适用于elasticsearch-py。
from elasticsearch import Elasticsearch
es = Elasticsearch('127.0.0.1:9200')
for index in es.indices.get('*'):
  print(index)

"""
import hashlib
from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from elasticsearch_dsl import Search, Q


# from typing import


class tkitElasticsearch():
    """


    """

    # es = Elasticsearch()
    # es = Elasticsearch('127.0.0.1:9200')
    def __init__(self, host='127.0.0.1:9200', index="tkit-index"):
        """
        #创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
        #这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
        es.indices.create(index='my-index',ignore)


        """
        self.es = Elasticsearch(host)
        indexList = []
        # for index in self.es.indices.get('*'):
        #     # print(index)
        #     pass
        self.index = index
        # self.es.indices.create(self.index, ignore)
        if self.index not in self.es.indices.get('*'):
            try:
                self.es.indices.create(self.index)
            except:
                pass
        else:
            pass
        # res = es.index(index="pet-index", id=one['path'], body=one)
        pass

    def getId(self, string):
        """
        md5 id

        :param string:
        :return:
        """
        string = str(string)
        # print(string)
        # 对要加密的字符串进行指定编码
        string = string.encode(encoding='UTF-8')
        # md5加密
        # print(hashlib.md5(string))
        # 将md5 加密结果转字符串显示
        string = hashlib.md5(string).hexdigest()
        # print(string)
        return string

    def add(self, item):
        """

        :param item:
        :return:
        """
        # item['path'] = item['id']
        # del one['_id']
        # print(item)
        myid = self.getId(item['id'])
        # del item['id']
        item["timestamp"] = datetime.now()
        try:
            # res = self.es.update(index=self.index, id=myid, body=item)
            # print(res['result'])
            res = self.es.index(index=self.index, id=myid, body=item)
        except Exception as e:
            print("错误", e)
            # res = self.es.update(index=self.index, id=myid, body=item)
            pass

    def gendata(self, items):
        # mywords = ['foo', 'bar', 'baz']
        out = []
        for item in items:
            myid = self.getId(item['id'])
            item["timestamp"] = datetime.now()
            item["_index"] = self.index
            item["_id"] = myid
            yield item
            # yield {
            #     "_index": self.index,
            #     "_id": myid,
            #     "body": item
            # }
        #     out.append({
        #         "_index": self.index,
        #         "id": myid,
        #         "body": item
        #     })
        # return out

    def addMulti(self, items):
        """

        https://www.elastic.co/guide/en/elasticsearch/reference/6.8/multi-index.html#multi-index
        https://stackoverflow.com/questions/61580963/insert-multiple-documents-in-elasticsearch-bulk-doc-formatter
        https://elasticsearch-py.readthedocs.io/en/master/helpers.html

        :return:
        """
        # print("add")
        successes = 0
        # bulk(self.es, self.gendata(items), refresh=True)
        for ok, action in streaming_bulk(
                client=self.es, index=self.index, actions=self.gendata(items), chunk_size=500, refresh="true"
        ):
            # progress.update(1)
            successes += ok
            # print(ok, action)

    # def addMulti(self, items):
    #     """
    #
    #     https://www.elastic.co/guide/en/elasticsearch/reference/6.8/multi-index.html#multi-index
    #     https://stackoverflow.com/questions/61580963/insert-multiple-documents-in-elasticsearch-bulk-doc-formatter
    #     https://elasticsearch-py.readthedocs.io/en/master/helpers.html
    #
    #     :return:
    #     """
    #
    #     # bulk(self.es, self.gendata(items))
    #     number_of_docs = 0
    #     # print("Indexing documents...")
    #     # progress = tqdm.tqdm(unit="docs", total=number_of_docs)
    #     successes = 0
    #     for ok, action in streaming_bulk(
    #             client=self.es, index=self.index, actions=self.gendata(items), chunk_size=1, refresh="true"
    #     ):
    #         # progress.update(1)
    #         successes += ok
    #     # print("Indexed %d/%d documents" % (successes, len(items)))

    def reindex(self):
        # reindex(client=self.es, source_index=self.index)
        pass

    def find(self, keyword, limit=50, fields=['content']):
        """
        搜索引擎


        :param keyword:
        :param limit:
        :return:
        """
        # client = Elasticsearch()
        # https: // elasticsearch - dsl.readthedocs.io / en / latest / search_dsl.html
        q = Q("multi_match", query=keyword, fields=fields)
        # print(q)
        # s = Search(using=self.es, index=self.index).query(q)
        # print(dir(s))
        # s = s[0:limit]
        # s = s.highlight_options(order='score')
        # s = s.highlight('content')
        # for it in s.execute():
        #     print(it)

        # s = Search(using=self.es, index="pet-index").query("match", content=keyword)
        s = Search(using=self.es, index=self.index).query(q)
        # s = Search(using=self.es, index=self.index).query("fuzzy", content=keyword)
        s = s[0:limit]
        s = s.highlight_options(order='score')
        s = s.highlight('content')
        response = s.execute()
        return response

    def save(self):
        self.es.indices.refresh(index=self.index)


if __name__ == '__main__':
    pass
