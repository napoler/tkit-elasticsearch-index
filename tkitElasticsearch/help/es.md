## ElasticSearch ClusterBlockException[blocked by: [FORBIDDEN/12/index read-only / allow delete (api)]

https://stackoverflow.com/questions/48155774/elasticsearch-read-only-allow-delete-auto-setting
执行接口
> curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
>
> curl -XPUT -H "Content-Type: application/json" http://localhost:9200/tkit-index-test/_settings -d '{"index.blocks.read_only_allow_delete": null}'





curl -POST -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"
index.blocks.read_only_allow_delete": null}'





