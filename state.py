# This script has methods for saving and loading the state
import configparser
import os
import sys
# Load param file and check validity
configPath = 'Specific/state.cfg'

def getConfig():
    stateConfig = configparser.ConfigParser()
    if not os.path.isfile(configPath):
        sys.exit("State file missing")
    stateConfig.read(configPath)
    if not 'State' in stateConfig:
        sys.exit("Invalid state file") 
    return stateConfig

def getSection(section):
    return getConfig()[section]

#Define some methods for reading and writing

def getCurrentState():
    return getSection('State')['current']

def getLastState():
    return getSection('State')['last']

def setCurrentState(new_state):
    stateConfig = getConfig()
    stateSection = stateConfig['State']
    stateSection['last'] = stateSection['current']
    stateSection['current'] = new_state
    with open(configPath, 'w') as configfile:
        stateConfig.write(configfile)

