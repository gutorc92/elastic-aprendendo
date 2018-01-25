from datetime import datetime
from elasticsearch import Elasticsearch
import codecs

es = Elasticsearch()

text = ""

with codecs.open("DJ17_2018-ASSINADO.txt","r", "utf-8") as handle:
    for line in handle.readlines():
        text += line 

text = text[:2000]

doc = {
    'text': text,
    'timestamp': datetime.now(),
}
res = es.index(index="diario-index", doc_type='diario', id=1, body=doc)
print(res)

res = es.get(index="diario-index", doc_type='diario', id=1)
print(res['_source'])

es.indices.refresh(index="diario-index")

res = es.search(index="diario-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(text)s" % hit["_source"])
