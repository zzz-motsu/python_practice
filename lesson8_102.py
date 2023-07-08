import os
# import subprocess
#
# s = subprocess.run(['dir', '|', 'findstr', 'test'], shell=True, stdout=subprocess.PIPE).stdout.decode('cp932')
# print(s)
#
# r = subprocess.run('dira' ,shell=True, check=True)
# print(r.returncode)
#
#

import subprocess

p1 = subprocess.Popen('dir *', stdout=subprocess.PIPE, shell=True)
p2 = subprocess.Popen(
    'find "test"', stdin=p1.stdout, stdout=subprocess.PIPE, shell=True
)
p1.stdout.close()
output = p2.communicate()[0]
print(output.decode('cp932'))