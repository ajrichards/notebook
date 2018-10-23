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
import pprint
import os,json
from datetime import datetime
from elasticsearch import Elasticsearch

pp = pprint.PrettyPrinter(indent=4)

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

result = es.search(index="test-index", body={"query": {"match_all": {}}})
#print("Got %d Hits:" % res['hits']['total'])
#for hit in res['hits']['hits']:
#    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

## show how to save the query to disk                                                                                        
json_file = "query.json"
json_filepath = os.path.join(".",json_file)
fh = open(json_filepath,'w')
json.dump(result,fh)
fh.close()

## show how to read back in the json
with open(json_filepath) as f:                                                                                                       
    data = json.load(f) 

pp.pprint(data)
    
