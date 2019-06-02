from nltk.corpus import wordnet

def similarity( w1, w2 ):
    w1 = wordnet.synset(w1)
    w2 = wordnet.synset(w2)
    print( w1, w2, w1.wup_similarity( w2 ) )


similarity("ship.n.01", "boat.n.01")

similarity("ship.n.01", "car.n.01")

similarity("ship.n.01", "vehicle.n.01")

similarity("sheep.n.01", "goat.n.01")

similarity("sheep.n.01", "animal.n.01")
