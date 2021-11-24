#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,subprocess,threading

class RunSubprocess(object):
    """
    a generic class 
    """

    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
        self.stdOut,self.stdErr = None,None

    def run(self,timeout=100):
        def target():
            self.process = subprocess.Popen(self.cmd,shell=True,stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE,universal_newlines=True,bufsize=4096)

            self.stdOut, self.stdErr = self.process.communicate()

        self.thread = threading.Thread(target=target)
        self.thread.start()

        ## wait a specified amount of time before terminating
        if timeout != None:
            self.thread.join(timeout)
            if self.thread.is_alive():
                print 'The subprocess was auto-terminated due to timeout'
                print "...", self.process.poll()
                self.process.terminate()
                self.thread.join()
        
            return self.process.returncode
        return None

    def terminate(self):
        if self.thread.is_alive():
            self.process.terminate()
            self.thread.join()

if __name__ == '__main__':
    
    myProcess1 = RunSubprocess("echo 'Process started'; sleep 10; echo 'Process finished'")
    myProcess2 = RunSubprocess("echo 'Process started'; sleep 2; echo 'Process finished'")

    print 'running 1'
    returnCode1 = myProcess1.run()
    print 'running 2'
    returnCode2 = myProcess2.run()

    #print myProcess2.process.poll():
    #    print("...waiting")
    #myProcess1.terminate()

    print myProcess1.stdOut
    print myProcess2.stdOut
    
    #print 'pass return code', returnCode

    ## test should fail
    #returnCode = myProcess.run(timeout=1)
    #print 'fail return code', returnCode

    #returnCode = myProcess.run(timeout=10)
    #myProcess.terminate()
    #print myProcess.stdOut
    

    
