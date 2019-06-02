from nltk.tokenize import sent_tokenize, word_tokenize

sample_text = "Hello Mr. Wosimosi, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print("Sentense tokens: ")
print(sent_tokenize(sample_text))

print()

print("Word tokens: ")
print(word_tokenize(sample_text))

print()
print("Iterating word tokens: ")
for i in word_tokenize(sample_text):
  print(i)
