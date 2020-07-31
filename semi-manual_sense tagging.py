#manual annotation of sense tags
#This is a simple example
#One can implement this to any other language
#Need a sense dictionary -dict like below

import nltk
dict={'bank':['0:money','1:shore'],'book':['0:read','1:ticket']}

print(dict)
pws=list(dict.keys())
print(pws)

for w in pws:
    print(dict[w])

line='bank is open to book an appointment'

lw=nltk.word_tokenize(line)
for w in lw:
    if w in pws:
        print('senses of',w,'are',dict[w])
        i=input('enter sense index')
        lw[lw.index(w)]=w+'('+dict[w][int(i)]+')'
        
    
print(' '.join(lw))

# output        
'''
{'bank': ['0:money', '1:shore'], 'book': ['0:read', '1:ticket']}
['bank', 'book']
['0:money', '1:shore']
['0:read', '1:ticket']
senses of bank are ['0:money', '1:shore']
enter sense index0
senses of book are ['0:read', '1:ticket']
enter sense index1
bank(0:money) is open to book(1:ticket) an appointment
'''
