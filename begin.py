#This is run on startup. First, pull the git repo. Then start the pacemaker.py in a different process. If pacemaker receives an update command, it will pull and then restart, which will update this script.
from pacemaker import startPacemaker
from git_operations import pullRemote
import subprocess as sp

pullRemote()

pacemakerProcess = sp.Popen(['python', 'pacemaker.py'], stdout=sp.PIPE)
