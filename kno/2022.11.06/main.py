from nltk.corpus import wordnet
import networkx as nx
import matplotlib.pyplot as plt

def closure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()
    
    def recurse(s):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name())
            for s1 in fn(s):
                graph.add_node(s1.name())
                graph.add_edge(s.name(), s1.name())
                recurse(s1)
                
    recurse(synset)
    return graph


nouns = ["cow", "grass", "foal", "meadow", "tree", "herd"]
verbs = ["eat", "stand"]
adjectives = ["small", "young"]

common = nouns + verbs +adjectives

for word in common:
       print(word, "--------------")
       syn = wordnet.synsets(word)[0]
       graph = closure_graph(syn,
                            lambda s: s.hypernyms())
       nx.draw_networkx (graph)
       plt.show()

       print(len(wordnet.synsets(word, pos='n')))
       print(len(wordnet.synsets(word, pos='a')))
       print(len(wordnet.synsets(word, pos='v')))

# from nltk.corpus import wordnet as wn
# import networkx as nx
# import matplotlib.pyplot as plt

# def closure_graph(synset, fn):
#     seen = set()
#     graph = nx.DiGraph()
    
#     def recurse(s):
#         if not s in seen:
#             seen.add(s)
#             graph.add_node(s.name())
#             for s1 in fn(s):
#                 graph.add_node(s1.name())
#                 graph.add_edge(s.name(), s1.name())
#                 recurse(s1)
                
#     recurse(synset)
#     return graph

# dog = wordnet.synset('dog.n.01')

# graph = closure_graph(dog,
#                       lambda s: s.hypernyms())

# nx.draw_networkx(graph)
# plt.show()

# word = "foal"
# syn = wordnet.synsets(word)
# print(len(syn))

# print("Synset name :  ", syn.name())

# print("\nSynset abstract term :  ", syn.hypernyms())

# print("\nSynset specific term :  ",
#        syn.hypernyms()[0].hyponyms())

# syn.root_hypernyms()

# print("\nSynset root hypernerm :  ", syn.root_hypernyms())

# print(len(wordnet.synsets(word, pos='n')))
# print(len(wordnet.synsets(word, pos='a')))
# print(len(wordnet.synsets(word, pos='v')))

