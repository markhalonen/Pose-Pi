import os
from git import Repo

repo = Repo(os.getcwd())

assert not repo.bare

origin = repo.remotes.origin

print(origin.pull())
