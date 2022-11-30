# Zadanie - wariant 1 (Emocje na twitterze)
# Ściągnij bazę przynajmniej kilku tysięcy tweetów z wybranym #hashtagiem (np. #ukraine lub #kaczynski lub #christmas). 
# Obrób tweety technikami modelu bag-of-words, przefiltruj i zostaw najczęstsze i najciekawsze. Zobrazuj je na wykresie słupkowym i w chmurze tagów.
# Podziel te tweety na pozytywne i negatywne, i dla każdej grupy zrób osobne chmury tagów. Czy się znacząco różnią? Być może podzielić tweety na więcej grup?
# Czy chmury tagów mają spójną tematykę? Sprawdź podobieństwa wyrazów stosując np. WUP similarity i przedstaw to w ciekawej formie.

import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet

nltk.download('stopwords')
nltk.download('vader_lexicon')

def getTweetsByHashtag(hashTag: str, near: str = "Gdansk", howMuch: int = 100, since: str = "2022-01-01", until: str = "2022-12-31", lang: str = "en"):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterHashtagScraper('#{} since:{} until:{}  lang:{} '.format(hashTag, since, until, lang)).get_items()):
        if i > howMuch:
            break
        tweets.append(
            [tweet.id, tweet.user.username, tweet.date, tweet.content, tweet.lang])
    return tweets
def count_tweets_between_date(tweets, start, stop):
    counter = 0
    for tweet in tweets:
        if(start<=tweet[2]<=stop):
            counter+=1

def filter_sentence(sentence, *words):
    list_n = []
    for e in sentence:
        e = e.replace('.', '')
        e = e.replace(',', '')
        e = e.replace('?', '')
        e = e.replace('!', '')
        e = e.replace('https', '')
        e = e.replace(';', '')
        e = e.replace('"', '')
        e = e.replace('\\', '')
        e = e.replace('/', '')
        e = e.replace(':', '')
        list_n.append(e)


    stop_words = set(stopwords.words('english'))
    for word in words:
        stop_words.add(word)
    return [w for w in list_n if not w in stop_words]


def lemaitze(word_list):
    l = []
    for words in word_list:
        l.append([WordNetLemmatizer().lemmatize(w) for w in words])
    return l

def countWords(wordsLists):
    counter = dict()
    for list in wordsLists:
        for word in list:
            counter[word]=counter.get(word, 0) + 1
    return counter

def mergeWordsFromDics(dictWithWords):
    string = ''
    for key, value in dictWithWords.items():
        string += key.lower()+" "
    return string

def is_positive(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    if sentiment_dict['compound'] >= 0.4:
        return True
    elif sentiment_dict['compound'] <= - 0.05:
        return False

def merge_list(list):
    string = ""
    for word in list:
        for w in word:
            string+=w
    return string

def draw_tag_cloug(words):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(words)
 
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    
    plt.show()

def main():

    english_tweets = pd.DataFrame(getTweetsByHashtag(hashTag="ukraine", since="2022-01-01", until="2022-12-31"),
                        columns=['Tweet Id', 'Username', 'Datetime', 'Text', "Language"])
    # print(count_tweets_between_date(english_tweets, datetime("2022-01"), datetime("2022-02")))
    # print(english_tweets)
    normalised_sentences = []
    for sentence in english_tweets['Text']:
        normalised_sentences.append(filter_sentence(sentence.split(" "), "Ukraine", "t", "#Ukraine","#Ukraine,", 'the', 'and', ',', '.', ';', '-', "''", "'s", "``", ""))
    lemaitzed = lemaitze(normalised_sentences)

    letter_counts = countWords(lemaitzed)
    letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    # print(letter_counts)
    comment_words = mergeWordsFromDics(letter_counts)
    draw_tag_cloug(comment_words)
    
    plt.show()

    neg =[]
    pos = []

    for sentence in lemaitzed:
        if is_positive(" ".join(sentence)):
            pos.append(sentence)
        else:
            neg.append(sentence)

    comment_words = merge_list(neg)
    draw_tag_cloug(comment_words)
    comment_words = merge_list(pos)
    draw_tag_cloug(comment_words)
    
    # for list in lemaitzed:
    #     print(list)
    #     sum = 0.0
    #     for j in range(0, len(list)):
    #         print(list[j])
    #         cb = wordnet.synset(list[3])[0]
    #         print(cb)
    #         for i in range(0, len(list)):
    #             if i != j:
    #                 ib = wordnet.synset(list[i])[0]
    #                 sum+=cb.wup_similarity(ib)

    #     print(sum/(len(list)-1))
main()