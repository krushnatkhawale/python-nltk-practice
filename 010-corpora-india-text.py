from nltk.corpus import indian
from nltk.tokenize import sent_tokenize


sample_text = indian.raw("marathi.pos")
marathi_text = sent_tokenize( sample_text )

print("Below is marathi text: (this is not proper way of reading text)")
print( marathi_text[0:5] )
