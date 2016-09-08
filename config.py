import configparser
import os
# Load param file and check validity
config = configparser.ConfigParser()
configPath = 'Specific/config.cfg'
if not os.path.isfile(configPath):
    print("Configuration incorrect")
    sys.exit("Config file missing")
config.read(configPath)
if not 'params' in config:
    sys.exit("Invalid params file") 
params = config['params']
if not all (k in params for k in ('id', 'tag', 'hw_type')):
    sys.exit('Missing params in param file')

def writeTag(tag):
    params['tag'] = tag
    print("Setting tag to: " + tag)
    with open(configPath, 'w') as configfile:
        config.write(configfile)
    
def readTag():
    return params['tag']

def readId():
    return params['id']

def readHwType():
    return params['hw_type']
