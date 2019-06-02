
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample_text = gutenberg.raw("bible-kjv.txt")

bible_text = sent_tokenize(sample_text) 


print("Text from bible is as follows: ")
print( bible_text[0:5] )

