#This is run on startup. First, pull the git repo. Then start the pacemaker.py in a different process. If pacemaker receives an update command, it will pull and then restart, which will update this script.
from git_operations import pullRemote, stash
import subprocess as sp
import time
import boto3
from triggerUpdateTagLambda import triggerUpdateTag
#Update from github
stash()
pullRemote()

sp.Popen(['python', 'pacemaker.py'])
print("Begin exiting")

time.sleep(4)

# Update this tag
triggerUpdateTag()
