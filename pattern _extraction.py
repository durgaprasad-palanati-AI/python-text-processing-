#print the text in line which folowed by 'number:'

import re

line=['1:abc','32:bcd','1456:xyz']

for i in range(0,len(line)):
      l=re.sub(r'\d',"",line[i])
      l=re.sub(r':',"",l)
      print(l)
 
#output
'''
abc
bcd
ABC
cde
'''
