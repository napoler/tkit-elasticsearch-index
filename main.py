# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press 双击 Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime

from tkitElasticsearch import tkitElasticsearch

es = tkitElasticsearch(host='127.0.0.1:9200', index="tkit-index-test1")
item = {"id": "22", "content": "鸡新城疫的实验室诊断方法有哪些"}
for it in range(2):
    print(datetime.now())
    item["id"] = datetime.now()
    item["content"] = item["content"] + str(it)
    es.add(item)
es.save()

# addMulti
items = []
for it in range(2):
    print(datetime.now())
    item["id"] = datetime.now()
    item["content"] = item["content"] + str(it)
    # es.add(item)
    items.append(item)
es.addMulti(items)
es.save()

for it in es.find("鸡新", limit=2, fields=['content']):
    print(dir(it))
    print(it)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
