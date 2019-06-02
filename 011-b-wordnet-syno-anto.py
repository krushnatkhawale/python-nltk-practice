from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append( l.name() )
        if(l.antonyms()):
            antonyms.append( l.antonyms()[0].name() )
synonyms = set(synonyms)
antonyms = set(antonyms)

print( synonyms, " ", len(synonyms) )

print( antonyms, " ", len(antonyms) )
