#!/usr/bin/env python

import time,os,csv,sys
from datetime import date
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split

    
## import some data to play with
iris = datasets.load_iris()

## Take only the first two features
X = iris.data[:,:2]
y = iris.target

## Perform a train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

## Specify parameters and model
params = {'C':1.0,'kernel':'linear','gamma':0.5}
clf = svm.SVC(**params,probability=True)

## fit model
clf = clf.fit(X_train, y_train)

## simulate a query
query = X_test[0,:]
if len(query.shape) == 1:
    query = query.reshape(1, -1)

## make prediction and gather data for log entry
time_start = time.time()
y_pred = clf.predict(query)
y_proba = None
if 'predict_proba' in dir(clf) and clf.probability == True:
    y_proba = clf.predict_proba(query)
m, s = divmod(time.time()-time_start, 60)
h, m = divmod(m, 60)
runtime = "%03d:%02d:%02d"%(h, m, s)
MODEL_VERSION = 1.0

## name the logfile using something that cycles with date (day, month, year)    
today = date.today()
month,day,year  = today.month, today.day, today.year
logfile = "aavail-churn-{}.log".format(month)

## write the data to a csv file    
header = ['unique_id','timestamp','y_pred','y_proba','x_shape','model_version','runtime']
write_header = False
if not os.path.exists(logfile):
    write_header = True
with open(logfile,'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|')
    if write_header:
        writer.writerow(header)

    to_write = map(str,['lklkj',time.asctime(),y_pred,y_proba,query.shape,MODEL_VERSION,runtime])
    writer.writerow(to_write)

sys.exit()    
print(dir(clf))
print(y_pred)




request_unique_id = None
timestamp = None
prediction = y_pred
input_matrix_summary = None
model_version_number = None



sys.exit()
expId = 'foo'
fidLog = open("%s.log"%(expId),'w')
log = csv.writer(fidLog)
log.writerow(["timestamp",time.asctime()])
fidLog.close()
os.system("cat %s.log"%expId)
os.system("rm %s.log"%expId)
sys.exit()

request_unique_id
timestamp
prediction
probability
input_matrix_summary
model_version_number
