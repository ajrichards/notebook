#!/usr/bin/env python

import time,os,csv

expId = 'foo'
fidLog = open("%s.log"%(expId),'w')
log = csv.writer(fidLog)
log.writerow(["timestamp",time.asctime()])
fidLog.close()
os.system("cat %s.log"%expId)
os.system("rm %s.log"%expId)
