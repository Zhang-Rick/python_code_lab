#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/22/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('~ee364/DataFolder/Lab03')

filename = os.path.join(DataPath,'coordinates.dat')
with open(filename) as f:
    lines=f.read().splitlines()
k=lines[3].strip()
print(k)
g = k.split(' ')
print(g)
h=list(filter(None,g))
print(h)