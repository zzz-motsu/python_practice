import os
import subprocess

s = subprocess.run(['dir', '|', 'findstr', 'test'], shell=True, stdout=subprocess.PIPE).stdout.decode('cp932')
print(s)

r = subprocess.run('dira' ,shell=True, check=True)
print(r.returncode)



