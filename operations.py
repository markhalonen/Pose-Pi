import os
import boto3
import json
import configparser
import sys
from subprocess import call
from picamera import PiCamera
from drawText import setText
s3 = boto3.resource('s3')

camera = PiCamera()

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
    
def handle_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))
    payload = toJSON(msg.payload.decode("utf-8"))
    if "command" in payload and "args" in payload:
        # Check and see if it's the appropriate hardware_id!!! This or make a channel for each iot device.
        if payload["command"] == "snap" :
            if checkSnapCommandFormat(payload):
                if payload["args"]["hw_id"] == readId():
                    
                    key = payload["args"]["photo_event_id"] + '.jpg'
                    print(key)
                    print('Taking photo...')
                    photoLocation = savePhoto(key)
                    if params['hw_type'] == 'pi':
                        data = open(photoLocation, 'rb')
                    else:
                        data = open('SampleImages/example_image_rosetta.jpg', 'rb')
                    s3.Bucket('pose-photos').put_object(Key=key, Body=data, ACL='public-read', ContentType='image/png')
                else:
                    print("Not my id!")
                    print(readId())
                    print(payload["args"]["hw_id"])		
            else:
                print("ERR: Invalid snap command!")
        elif(payload["command"] == "updateTag"):
            if checkUpdateTagCommandFormat(payload):
                if payload["args"]["hw_id"] == readId():
                    new_tag = payload["args"]["new_tag"]
                    writeTag(new_tag)
                    setDisplayText(new_tag)
                    print("Updating tag.")
            else:
                print("ERR: Invalid updateTag command!");
        elif(payload["command"] == "updateSoftware"):
            pass #Print "Update me!"
    else:
        print("Invalid payload format")
        
def checkSnapCommandFormat(snapCommand): #TODO: Use json schema
    return ("command" in snapCommand and snapCommand["command"] == "snap" and "args" in snapCommand 
    and "photo_event_id" in snapCommand["args"] and "hw_id" in snapCommand["args"])
    
def checkUpdateTagCommandFormat(updateCommand):
    return ("command" in updateCommand and updateCommand["command"] == "updateTag" and "args" in updateCommand 
    and "hw_id" in updateCommand["args"] and "new_tag" in updateCommand["args"])

def savePhoto(name):
    location = 'Images/' + name
    camera.capture(location)
    return location

def setDisplayText(text):
    setText(text)
    
def toJSON(s):
    return json.loads(s)
