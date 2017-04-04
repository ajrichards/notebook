#!/usr/bin/env python
"""
populate the mongodb database

 * 'documents' are stored in collections
 * collections are analogous to tables in relational databases
 * collection does not require its documents to have the same schema
 * lets define a document as an interaction with subject or subject data

sudo apt-get install mongodb
sudo pip install pymongo

"""

import sys,csv,os,re
from pymongo import MongoClient
import numpy as np

## connect or create db if it does not exist
client = MongoClient()
db = client['my-bcplatform']
knownFields = set([])
collection = db['familial']
collection = db['sporadic']

## clean the database
db['familial'].remove({})
db['sporadic'].remove({})

## data munge functions
def read_data(filePath,splitDx=False):
    """
    read csv file
    """

    ## error check the file header
    fid = open(filePath,'rU')
    reader = csv.reader(fid,delimiter=",")
    header = reader.next()
    header = [re.sub("\s+","_",x.lower()) for x in header]
    print("...reading %s"%filePath)
    if header[-1] == '':
        header = header[:-1]
    if '' in header:
        raise Exception("blank found in header")
    if len(list(set(header))) != len(header):
        print(filePath)
        print(header)
        header = np.array(header)
        print("non-unique")
        for h in np.unique(header):
            indices = np.where(header == h)[0]
            if indices.size > 1:
                print header[indices]
        raise Exception("header is not unique") 
    results = {}
    newFields = [h for h in header if h not in knownFields]
    print("......INFO: adding new fields: %s"%";".join(newFields))
    knownFields.update(header)

    ## read data in
    for col in header:
        results[col] = []

    for linja in reader:
        if len(linja) > len(header) and linja[-1] == '':
            linja = linja[:-1]
        if len(linja) != len(header):
            print(linja)
            print len(linja), len(header)
            raise Exception("bad line")
        for c in range(len(header)):
            if re.search("dx",linja[c]):
                linja[c] = re.sub("\s+","_",linja[c])

            if splitDx and header[c] == 'primary_dx':
                linja[c] = linja[c].lower()
                dx = re.sub("probable|possible|definate","",linja[c])
                print len(linja),linja[c],"...", dx
                if dx[-1]=="_":
                    dx = dx[:-1]
                results['primary_dx'].append(dx)
            else:
                results[header[c]].append(linja[c])
    return results

def insert_documents(results,fileShort,csvInserted):

    if fileShort in csvInserted:
        raise Exception("WARNING: another csv with %s was found --- archive the oldest one"%fileShort) 
        
    doc = {}
    
    ## error check
    numElements = None
    for key,item in results.iteritems():
        if not numElements:
            numElements = len(item)
            continue
        if len(item) != numElements:
            print("%s,%s,%s"%(key,numElements,len(item)))
            raise Exception("unbalanced dictionary")

    ## loop through the documents
    for n in range(numElements):
        toInsert = {}
        subject = results["subject"][n]
        tokens = subject.split("-")
        origin = None
        family = None
        member = None

        if re.search("[nj|va|da]-",subject):
            dbtype = 'familial'
        else:
            dbtype = 'sporadic'

        if re.search("9991",subject):
            dbtype = 'sporadic'

        if dbtype == 'familial':
            if len(tokens) > 1:
                origin = tokens[0]
                family = "%s-%s"%(tokens[0],tokens[1])
                member = None
            if len(tokens) > 2:
                origin = tokens[0]
                family = "%s-%s"%(tokens[0],tokens[1])
                member = tokens[2]

        if origin:
            toInsert["origin"] = origin
        if family:
            toInsert["family"] = family
        if member:
            toInsert["member"] = member

        toInsert['file'] = fileShort

        for key in results.iterkeys():
            toInsert[key] = results[key][n]
        
        ## insert document
        db[dbtype].insert_one(toInsert)

## scan through the files and upload them to mongodb
dataDir = os.path.join(".","data")

for fileName in os.listdir(dataDir):#["cap_2015-09-03.csv","clin-core_2015-10-22.csv"]:
    filePath = os.path.join(dataDir,fileName)
    fileShort = fileName.split("_")[0]
    if fileShort in ['clin-core']:
        splitDx = True
    else:
        splitDx = False

    results = read_data(filePath,splitDx=splitDx)
    csvInserted = []
    insert_documents(results,fileShort,csvInserted)


#print("data base populated")
#print(sorted(knownFields))
#print results.keys()



###################################################
## print a summary of the collections
for collection in ['familial','sporadic']:
    
    ## get unique ids
    cursor = db[collection].find()
    subjects = np.unique(np.array([c["subject"] for c in cursor]))
    
    ## get basic info associated with each unique ids
    for sbj in subjects:
        cursor = db[collection].find({"subject": "CA-9991-105"})

    print("collection: %s"%collection)
    print("\tdocuments: %s"%db[collection].count())
    print("\tunique ids %s"%len(subjects))

#print(db['familial'].count())
#db['sporadic'].count()

sys.exit()
##############################################################
client = MongoClient()
db = client['primer']

print db.collection_names()
print db['dataset']
#print(dir(db))

from datetime import datetime
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

print result.inserted_id
cursor = db.restaurants.find()


for document in cursor:
    print(document)

cursor = db.restaurants.find({"borough": "Manhattan"})
for document in cursor:
    print(document)

cursor = db.restaurants.find({"address.zipcode": "10075"})
for document in cursor:
    print(document)

cursor = db.restaurants.find({"grades.grade": "B"})

print 'done'
