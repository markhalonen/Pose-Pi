import os
import boto3
import json
s3 = boto3.resource('s3')

tagDirectory = "Specific"
tagName = "tag.txt"
tagPath = os.path.join(tagDirectory, tagName)
idPath = "Specific/id.txt"

def writeTag(tag):
    if not os.path.isdir(tagDirectory):
        os.makedirs(tagDirectory)
    f = open(tagPath, 'w')
    f.write(tag)
    
def readTag():
    f = open(tagPath) # Should be checking to see if file exists
    return f.readline()

def readId():
    f = open(idPath) # Should be checking to see if file exists
    return f.readline()
    
def handle_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))
    payload = toJSON(msg.payload.decode("utf-8"))
    if "command" in payload and "args" in payload:
        # Check and see if it's the appropriate hardware_id!!! This or make a channel for each iot device.
        if payload["command"] == "snap" :
            if checkSnapCommandFormat(payload):
                if payload["args"]["hw_id"] == readId():
                    data = open('Images/example_image_rosetta.jpg', 'rb')
                    key = payload["args"]["photo_event_id"] + '.jpg'
                    print(key)
                    s3.Bucket('pose-photos').put_object(Key=key, Body=data, ACL='public-read', ContentType='image/png')
                else:
                    print("Not my id!")
            else:
                print("ERR: Invalid snap command!")
        elif(payload["command"] == "updateTag"):
            if "new_tag" in payload["args"]:
                writeTag(payload["args"]["new_tag"])
        elif(payload["command"] == "updateSoftware"):
            pass #Print "Update me!"
    else:
        print("Invalid payload format")
        
def checkSnapCommandFormat(snapCommand): #TODO: Use json schema
    return ("command" in snapCommand and snapCommand["command"] == "snap" and "args" in snapCommand 
    and "photo_event_id" in snapCommand["args"] and "hw_id" in snapCommand["args"])
    
def toJSON(s):
    return json.loads(s)