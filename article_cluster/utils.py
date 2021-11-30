import string
import pickle
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from pandas import Series


model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
mapping = {
    0: 'Entertainment',
    1: 'Politics',
    2: 'Tech',
    3: 'Business',
    4: 'Sports'
}

class CleanText:
    
    def remove_puntuaction(self, input_text):
        punct = string.punctuation
        trantab = str.maketrans(punct, len(punct)*' ')
        return input_text.translate(trantab)
    
    def to_lower(self, input_text):
        return input_text.lower()
    
    def remove_stopwords(self, input_text):
        stopwords_list = stopwords.words('english')
        words = input_text.split()
        clean_words = [word for word in words if (word not in stopwords_list) and len(word) > 1]
        return ' '.join(clean_words)
    
    def lemmatizing(self, input_text):
        lematize = WordNetLemmatizer()
        sentence_words = word_tokenize(input_text)
        stemmed_words = [lematize.lemmatize(word, pos='v') for word in sentence_words]
        return ' '.join(stemmed_words)
    
    def transform(self, X,):
        clean_X = X.apply(self.remove_puntuaction).apply(self.to_lower).apply(self.remove_stopwords).apply(self.lemmatizing)
        return clean_X
    
    def predict(self, X):
        x = X.apply(self.to_lower)
        x = X.apply(self.remove_puntuaction)
        x = X.apply(self.remove_stopwords)
        
        x = X.apply(self.lemmatizing)
        
        return x



def predict(words):
    cleaner = CleanText()
    my_x = vectorizer.transform(cleaner.predict(Series(words)))

    prediction =  model.predict(my_x)
    print(prediction)

    return mapping[prediction[0]]