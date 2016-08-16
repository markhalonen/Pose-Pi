# Starts the subscriber process and monitors it's output to see if it should be updated.
import subprocess as sp
import time
from state import getCurrentState

#Do a git clone and restart the pacemaker...

# Starts the process.
subscriberProcess = sp.Popen(['python', 'subscriber.py'], stdout=sp.PIPE)
print("Subsriber ID: " + str(subscriberProcess.pid))
#Monitor the process. If the process stops, try to restart it. If the state.cfg file says 'update', restart the pi.
for x in range(0,10):
    time.sleep(1)
    print(x)
    status = sp.Popen.poll(subscriberProcess)
    if status != None:
        #The process stopped, try to restart it.
        print("The process stopped! Trying to restart...")
        subscriberProcess = sp.Popen(['python', 'subscriber.py'], stdout=sp.PIPE)
        print("Subsriber ID: " + str(subscriberProcess.pid))
    
    if getCurrentState() == 'update':
        print('Needs to update!!!')    


subscriberProcess.kill()
