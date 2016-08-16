import os
from git import Repo

repo = Repo(os.getcwd())

assert not repo.bare

origin = repo.remotes.origin

def pullRemote():
    print(origin.pull())
