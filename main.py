import os 
import tweepy 
from dotenv import load_dotenv 
import re 
from nltk.corpus import stopwords 
from nltk. stem import WordNetLemmatizer 
import nltk 


nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('turkish'))



load_dotenv()




consumer_key = os.getenv('consumer_key')
consumer_key_secret = os.getenv('consumer_key_secret')
twitter_acces_token = os.getenv('twitter_acces_token')
twitter_acces_token_secret = os.getenv('twitter_acces_token_secret')


auth = (tweepy.OAuthHandler(consumer_key, consumer_key_secret, twitter_acces_token, twitter_acces_token_secret))

api = tweepy.API(auth)



                  

def fetch_tweets(query, count = 500):
    tweets = tweepy.Cursor(api.search, q=query, lang='tr').items(count) 
    tweets.text = [tweets.text for tweet in tweets ]
    return tweets.text 

tweets = fetch_tweets('python', 500) 

def preprocess_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if word not in stop_words]
    text = ''.join(text)
    return text 

clened_tweets = [preprocess_text(tweet) for tweet in tweets ]






