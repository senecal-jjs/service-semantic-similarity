from app.models import RssChannel
from collections import defaultdict
from gensim import corpora 
import gensim.downloader as api
# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
from nltk import download

download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('english')

def preprocess(sentence):
    return [w for w in sentence.lower().split() if w not in stop_words]

def generate_corpora():
    channels = RssChannel.query.all()

