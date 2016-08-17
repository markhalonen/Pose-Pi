#!/bin/bash
whoami
su -c "source  /home/pi/Pose-Pi/P3/bin/activate && python  /home/pi/Pose-Pi/Dev/s3upload.py" pi
#su -c "python  /home/pi/Pose-Pi/Dev/s3upload.py" pi
