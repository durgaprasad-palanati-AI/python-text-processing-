import nltk
import codecs

file=codecs.open('new2.txt','r','utf8')

fh=file.readlines()                     #['సతతహరిత', 'సమశీతోష్ణ', ' అడవి-ఇల్లు*అడవి ']-the line is stored in new1.txt
                                        #the king's cat is caught with kit's. -the line is stored in new2.txt

for line in fh:
    l=nltk.tokenize.word_tokenize(line)     

print(l)                           # ['[', "'సతతహరిత", "'", ',', "'సమశీతోష్ణ", "'", ',', "'", 'అడవి-ఇల్లు', '*', 'అడవి', "'", ']']
                                    #['\ufeffthe', 'king', "'s", 'cat', 'is', 'caught', 'with', 'kit', "'s", '.']
ll=[]                               #to store new updated token list
for i in l:
    if i[0]=='\'':
        ix=i.replace('\'','')
        ll.append(ix)
    else:
        ll.append(i)
                                                        #updated correct one's
print(ll)                           #['[', 'సతతహరిత', '', ',', 'సమశీతోష్ణ', '', ',', '', 'అడవి-ఇల్లు', '*', 'అడవి', '', ']']
                                    #['\ufeffthe', 'king', 's', 'cat', 'is', 'caught', 'with', 'kit', 's', '.']
