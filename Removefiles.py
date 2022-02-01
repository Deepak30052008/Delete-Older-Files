from importlib.metadata import files
import os
import shutil
from sys import path
from tabnanny import check
import time

path=input("Enter Your Path : ")
days=259200
duration=time.time()
checking=duration-days

if (os.path.exists(path)):
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            path=os.path.join(root,name)
            ctime=os.stat(path).st_ctime
            if (checking>=ctime):
                os.remove(path)
                print("\n Deleted the path" + path + "successfully")
        for name in dirs:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime
            if (checking >= ctime):
                shutil.rmtree(path)
                print("\n Deleted the path " + path + " successfully")
else:
    print("\n Path not found")
