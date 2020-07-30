#print the text in line which folowed by 'number:'

import re



line=['1:abc','2:bcd']

for i in range(0,len(line)):
    if re.search(r'\D',line[i]):
        print('---',line[i][2:])    #--- abc
                                    #--- bcd

