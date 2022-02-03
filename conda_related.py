import os
import sys
import subprocess

def get_conda_environments():
    conda_environments = subprocess.run(['conda', 'env', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return str(conda_environments.stdout)

if __name__ == '__main__':
    environments = get_conda_environments()

    print('done')
