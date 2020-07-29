#output stored in -new_poly_134.txt removes empty lines
import os
import polyglot
from polyglot.text import Text, Word
import codecs
import nltk
import sys

filename='new_poly_134.txt'



#remove emty lines
def remove_empty_lines(filename):

    with codecs.open(filename,'r','utf-8') as filehandle:
        lines = filehandle.readlines()

    with codecs.open(filename, 'w','utf-8') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)   
    filehandle.close()
remove_empty_lines(filename)


