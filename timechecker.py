import time
import os
import psutil
time.sleep(180)

PROCNAME = "SimplePassMngr.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()
print("task done")