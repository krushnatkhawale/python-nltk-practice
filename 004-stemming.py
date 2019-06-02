from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

sample_words = [ "python", "pythoner", "pythoning", "pythoned", "pythonly" ]

print("Sample words are: ")
print(sample_words)

print()
print("Stemmed words in above list are: ")
for word in sample_words:
  print( stemmer.stem(word) )

print()

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

print("new text is: ")
print(new_text)

print()
print("Stemmed word for each in word new text are: ")
for word in word_tokenize( new_text ):
  print( stemmer.stem( word ) )
