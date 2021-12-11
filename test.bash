# /bin/bash


curl -XGET -H "Content-Type: application/json" 'http://127.0.0.1:9200/chinese_sents/_search' -d '
{
    "query": {
        "match_all": {}
    }
}'


curl -XGET -H "Content-Type: application/json" 'http://127.0.0.1:9200/chinese_sents/_search' -d '
{
    "query": {
        "match": {"id":"细节"}
    }
}'


curl -XGET -H "Content-Type: application/json" 'http://127.0.0.1:9200/chinese_sents_next/_search' -d '
{
    "query": {
        "match": {"id":"细节"}
    }
}'
