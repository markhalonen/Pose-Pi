# Starts the subscriber process and monitors it's output to see if it should be updated.
import subprocess as sp
import time
import os
from state import getCurrentState, setCurrentState

subscriberProcess = sp.Popen(['python', 'subscriber.py'], stdout=sp.PIPE)
print("Subsriber ID: " + str(subscriberProcess.pid))
#Monitor the process. If the process stops, try to restart it. If the state.cfg file says 'update', restart the pi.
while True:
    time.sleep(1)
    status = sp.Popen.poll(subscriberProcess)
    if status != None:
        #The process stopped, try to restart it.
        print("The process stopped! Trying to restart...")
        subscriberProcess = sp.Popen(['python', 'subscriber.py'], stdout=sp.PIPE)
        print("Subsriber ID: " + str(subscriberProcess.pid))
    
    if getCurrentState() == 'update':
        print('Updating!!')
        setCurrentState('good')
        #restart the pi!
        os.system('sudo shutdown -r now')


subscriberProcess.kill()

