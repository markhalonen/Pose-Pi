import os
from git import Repo

repo = Repo('/home/pi/Pose-Pi')

assert not repo.bare

origin = repo.remotes.origin

def pullRemote():
    print(origin.pull())
