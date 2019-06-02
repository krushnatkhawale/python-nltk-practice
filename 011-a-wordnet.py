from nltk.corpus import wordnet

syns = wordnet.synsets("program")

# synset - synonym set
print("Synonyms set: syns")
print(syns)

# just one synonym
print("\nJust one: syns[0]")
print(syns[0])

# lemmas
print("\nAll lemmas: syns[0].lemmas()")
print(syns[0].lemmas())

# just one lemma
print("\nJust one lemma: syns[0].lemmas()[0].name()")
print(syns[0].lemmas()[0].name())

# definition
print("\nDefinition: syns[0].definition()")
print(syns[0].definition())

# examples
print("\nExamples: syns[0].examples()")
print(syns[0].examples())




print()
print("DONE")
