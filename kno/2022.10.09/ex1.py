from nltk.tokenize import word_tokenize
import helper
import matplotlib.pyplot as plt
from collections import Counter


file = helper.read_file('article1.txt')
word_tokens = word_tokenize(file)
print("after tokenized: ", len(word_tokens))
word_tokens = helper.filter_sentence(
    word_tokens, 'the', 'and', ',', '.', ';', '-', "''", "'s", "``")
print("after stop_words: ", len(word_tokens))

lemaitzed = helper.lemaitze(word_tokens)

# for i in range(0, len(lemaitzed)):
#     if (word_tokens[i] != lemaitzed[i]):
#         print(word_tokens[i], lemaitzed[i])
print("after lemaitzed: ", len(word_tokens))


letter_counts = dict(Counter([w.lower() for w in lemaitzed]).most_common(10))

plt.bar(list(letter_counts.keys()), list(letter_counts.values()))
plt.show()
