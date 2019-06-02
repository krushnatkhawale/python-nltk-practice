from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sample_sentense = "This is an example showing off stop word filteration."

# stopwords in english language
ex1 =  stopwords.words("english") 

# set of stopwords in english language
ex2 = set( stopwords.words("english") )

stop_words = ex2
words = word_tokenize( sample_sentense )

print("Standard stop words are: ")
print(stop_words)

print()

print("Words in given sentence are: ")
print(words)


filtered_words = []
for w in words:
  if w not in stop_words:
    filtered_words.append(w)

print()
print("Filtered words are: ")
print(filtered_words)

print()
print("Another way to filter these words: ")
print([w for w in words if not w in stop_words])
