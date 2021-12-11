import sys
# sys.path.append('../')

import jieba
import jieba.analyse
def findKeywords(text, topK=10):
    tags = jieba.analyse.extract_tags(text, topK=topK)
    return tags

# if withWeight is True:
#     for tag in tags:
#         print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
# else:
#     print(",".join(tags))