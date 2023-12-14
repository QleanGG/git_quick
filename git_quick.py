'''
This is a git script to add all files, commit and push filed to your repository on github
it takes the folder path from your os and enables to make the commits to your main branch.

This will only work on main branch as it is a quick short script
'''

import os
from git import Repo


try:
    git_path = os.getcwd()
    repo = Repo(git_path)
    assert not repo.bare

    # add all files but remove the script
    repo.index.add('*')
    repo.index.remove('git_quick.py')
    
    # commit with default msg
    commit_message = "Auto commit"
    repo.index.commit(commit_message)

    repo.git.push('origin', 'main')
    print("It is done!")
except Exception as e:
    print(f"An error occurred: {e}")