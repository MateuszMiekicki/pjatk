import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 

def read_file(fileName:str):
    with open(fileName, 'r') as file:
        return file.read().replace('\n', '')

def compute_tf(wordDict, doc):
    tfDict = {}
    corpusCount = len(doc)
    for word, count in wordDict.items():
        tfDict[word] = count/float(corpusCount)
    return(tfDict)

def make_dict(total_set:set, words:set):
    word_dict = dict.fromkeys(total_set, 0) 
    for word in words:
        word_dict[word]+=1
    return word_dict

def filter_sentence(sentence, *words):
    stop_words = set(stopwords.words('english'))
    for word in words:
        stop_words.add(word)
    return [w for w in sentence if not w in stop_words]

def lemaitze(word_list):
    return [WordNetLemmatizer().lemmatize(w) for w in word_list]