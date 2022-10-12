import snscrape.modules.twitter as sntwitter
import pandas as pd

#https://github.com/igorbrigadir/twitter-advanced-search
#https://github.com/JustAnotherArchivist/snscrape/blob/master/snscrape/modules/twitter.py
def getTweetsByHashtag(hashTag: str, near: str = "Gdansk", howMuch: int = 100, since: str = "2022-01-01", until: str = "2022-12-31", lang: str = "pl"):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterHashtagScraper('#{} since:{} until:{} near:"{}" lang:{} '.format(hashTag, since, until, near, lang)).get_items()):
        if i > howMuch:
            break
        tweets.append(
            [tweet.id, tweet.user.username, tweet.date, tweet.content, tweet.place.fullName, tweet.lang])
    return tweets

def main():
    tweets = pd.DataFrame(getTweetsByHashtag(hashTag="kaczynski", near="Gdansk", since="2022-06-01", until="2022-10-09"),
                        columns=['Tweet Id', 'Username', 'Datetime', 'Text', "Place", "Language"])
    print(tweets)

main()