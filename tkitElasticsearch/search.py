# -*- coding: utf-8 -*-
"""
作者：　terrychan
Blog: https://terrychan.org
# 说明：
借助eslai shixian sou suo


"""

import os
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import Q
import json


def search_sent_plus(keyword):
    client = Elasticsearch()
    q = Q("multi_match", query=keyword, fields=['title', 'content'])
    s = Search(using=client)
    # s = Search(using=client, index="pet-index").query("match", content="金毛")
    s = Search(using=client, index="pet-sent-index").query(q)
    s=s[0:50]
    s=s.highlight_options(order='score')
    s = s.highlight('content')
    response = s.execute()
    return response
def search_content(keyword,limit=50):
    """
    搜索引擎


    :param keyword:
    :param limit:
    :return:
    """
    client = Elasticsearch()
    q = Q("multi_match", query=keyword, fields=['title', 'content'])
    s = Search(using=client)
    # s = Search(using=client, index="pet-index").query("match", content="金毛")
    s = Search(using=client, index="pet-index").query(q)
    s=s[0:limit]
    s=s.highlight_options(order='score')
    s = s.highlight('content')
    response = s.execute()
    return response


if __name__ == '__main__':

    print(search_sent_plus("金毛"))
    pass
