from app.models import RssChannel
from collections import defaultdict
# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
from nltk import download
import gensim
import os

class WMD():
    def __init__(self):
        download('stopwords')  # Download stopwords list.
        self.stop_words = stopwords.words('english')
        self.model_path = os.path.join(os.getcwd(), 'app/lsi/GoogleNews-vectors-negative300.bin')
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.model_path, binary=True)

    def preprocess(self, sentence):
        return [w for w in sentence.lower().split() if w not in self.stop_words]

    def get_model(self):
        return self.model