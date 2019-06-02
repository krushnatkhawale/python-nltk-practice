from nltk.stem import WordNetLemmatizer

lemmatizer  = WordNetLemmatizer()


print("cats             :  " + lemmatizer.lemmatize("cats"))
print("cacti            :  " + lemmatizer.lemmatize("cacti"))
print("geese            :  " + lemmatizer.lemmatize("geese"))
print("rocks            :  " + lemmatizer.lemmatize("rocks"))
print("python           :  " + lemmatizer.lemmatize("python"))
print("pythoned         :  " + lemmatizer.lemmatize("pythoned"))
print("pythoners        :  " + lemmatizer.lemmatize("pythoners"))
print("pythonly         :  " + lemmatizer.lemmatize("pythonly"))

print()
print("--------------  lemmatize with pos  ---------------")
print()

print("better   with a  :  " + lemmatizer.lemmatize("better", pos='a'))
print("better   with v  :  " + lemmatizer.lemmatize("better", pos='v'))
print("better   with a  :  " + lemmatizer.lemmatize("better", 'a'))
print("better   with n  :  " + lemmatizer.lemmatize("better", 'n'))
print("good     with a  :  " + lemmatizer.lemmatize("good", pos='a'))
print("good     with v  :  " + lemmatizer.lemmatize("good", pos='v'))
print("good     with a  :  " + lemmatizer.lemmatize("good", 'a'))
print("good     with n  :  " + lemmatizer.lemmatize("good", 'n'))

