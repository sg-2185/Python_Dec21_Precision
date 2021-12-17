import os
import subprocess

OScommand = "echo Tinitiate.com"
os.system(OScommand)
subprocess.call(['echo','Hello Tinitiate'], shell=True)
(SDOut,SDErr) = subprocess.Popen( ['echo','Hello World!']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,universal_newlines = True
                                 ,shell=True).communicate()

print(SDOut)


