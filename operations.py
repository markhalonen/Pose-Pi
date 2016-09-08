import os
import boto3
import json
import config #config.py
import sys
import time
from subprocess import call
from picamera import PiCamera
from drawText import setText
from state import setCurrentState
s3 = boto3.resource('s3')

camera = PiCamera()
camera.vflip = False
    
def handle_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))
    payload = toJSON(msg.payload.decode("utf-8"))
    if "command" in payload and "args" in payload:
        # Check and see if it's the appropriate hardware_id!!! This or make a channel for each iot device.
        if payload["command"] == "snap" :
            if checkSnapCommandFormat(payload):
                if payload["args"]["hw_id"] == config.readId():
                    
                    key = payload["args"]["photo_event_id"] + '.jpg'
                    print(key)
                    print('Taking photo...')
                    sleepTime = 1
                    setDisplayText("5")
                    time.sleep(sleepTime)
                    setDisplayText("4")
                    time.sleep(sleepTime)
                    setDisplayText("3")
                    time.sleep(sleepTime)
                    setDisplayText("2")
                    time.sleep(sleepTime)
                    setDisplayText("1")
                    time.sleep(sleepTime)
                    setDisplayText("0")
		
                    photoLocation = savePhoto(key)
                    if config.readHwType() == 'pi':
                        data = open(photoLocation, 'rb')
                    else:
                        data = open('SampleImages/example_image_rosetta.jpg', 'rb')
                    s3.Bucket('pose-photos').put_object(Key=key, Body=data, ACL='public-read', ContentType='image/png')
                else:
                    print("Not my id!")
                    print(config.readId())
                    print(payload["args"]["hw_id"])		
            else:
                print("ERR: Invalid snap command!")
        elif(payload["command"] == "updateTag"):
            if checkUpdateTagCommandFormat(payload):
                if payload["args"]["hw_id"] == config.readId():
                    new_tag = payload["args"]["new_tag"]
                    config.writeTag(new_tag)
                    if config.readHwType() == 'pi':
                        setDisplayText(new_tag)
                    print("Updating tag.")
            else:
                print("ERR: Invalid updateTag command!");
        elif(payload["command"] == "updateSoftware"):
            setCurrentState('update')
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

setDisplayText(config.readTag())
