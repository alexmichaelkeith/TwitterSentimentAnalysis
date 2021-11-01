import tweepy
import pandas
import config
import matplotlib.pyplot as plt
from textblob import TextBlob


# Initialization
tweetDataframe = pandas.DataFrame()
sentimentDataframe = pandas.DataFrame()
# Authenticating with Twitter API
auth = tweepy.AppAuthHandler(config.get_consumer_key(), config.get_secret_key())
api = tweepy.API(auth)


def tweet_sentiment(tweet):

    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity


def search_tweets(keyword):
    tweets = []
    sentiment = []
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword).items(config.get_number_of_tweets_per_keyword()):
        tweet = tweet.text.replace('\n', '')
        tweets.append(tweet)
        sentiment.append(tweet_sentiment(tweet))

    return tweets, sentiment


def graph(keywords):
    plt.figure('Sentiment Graph')
    plt.bar(keywords, sentimentDataframe.mean(numeric_only=None))
    plt.title('Sentiment Graph')
    plt.xlabel('Keyword')
    plt.ylabel('Sentiment (-1,1) Scale')
    plt.savefig('SentimentGraph.png')
    if config.get_show_graph():
        plt.show()


def main():
    keywordsfile = open("keywords.txt", "r")
    keywords = keywordsfile.readlines()
    for keyword in keywords:
        tweetDataframe[keyword], sentimentDataframe[keyword] = search_tweets(keyword)

    tweetDataframe.to_csv('tweets.csv', index=False)
    sentimentDataframe.to_csv('tweets_sentiment.csv', index=False)
    graph(keywords)
    print('done')


if __name__ == "__main__":
    main()
