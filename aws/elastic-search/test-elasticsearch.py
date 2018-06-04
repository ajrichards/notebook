"""
INSTALL
~$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.deb
~$ sudo dpkg -i elasticsearch-6.2.4.deb 
~$ sudo apt-get install -f
~$ sudo apt-get update
~$ sudo apt-get upgrade

~$ pip install elasticsearch
"""

"""
THE SERVICE

if you want to ensure that it starts and stops with the server
sudo systemctl enable elasticsearch.service

At a minimum change the name and node id to configure the service
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04

Start it
sudo systemctl start elasticsearch

"""

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
