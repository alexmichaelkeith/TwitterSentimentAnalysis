# TwitterSentimentAnalysis

Python - tweepy bot used to scrape data from twitter keywords,
then uses machine learning to give each tweeet a sentiment score from (-1,1).
These tweets and setiment scores are saved as .csv files.
This data is then transformed and saved as a matplotlib bar chart.
Ensure your use case is permitted by twitter.
Do not abuse this script for spamming or other illegal purposes.

## Inital Setup

     1.) Apply for a twitter developer account here https://developer.twitter.com/en/apply-for-access
     2.) Login to your account and copy and paste the consumer key, and the consumer secret key into the config.py file.
     3.) Change the numberOfTweetsPerKeyword variable in config.py to whatever you would like. Default is 1000.
     4.) Change the keywords in keywords.txt to whatever you want.
     
     The script has the dependancies tweepy, pandas, textblob, and matplotlib.pyplot as python modules
     You can install these by doing the following : 
     # Enter the directory of the project and type in command line 
     ------------------------------------->
     1.)  pip install -r requirements.txt
    
## Running the script
    # Enter the directory of the project and type in command line
    ------------------------------------->
    1.) sudo python TwitterSentimentAnalysis.py
    2.) The tweets.csv, tweets_sentiment.csv, and the SentimentGraph.png file should be populated with all the twitter data that has been scraped
    
