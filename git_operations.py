import os
from git import Repo

repo = Repo('/home/pi/Pose-Pi')

assert not repo.bare

origin = repo.remotes.origin

def pullRemote():
    print(origin.fetch())
    print(repo.git.reset('--hard', 'origin/master'))

def stash():
    print(repo.git.stash('save'))
