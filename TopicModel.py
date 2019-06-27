# Databricks notebook source
import gensim
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import pickle
import nltk
import numpy as np
nltk.download('wordnet')


class TopicModel:
    def __init__(self, model_path, dictionary_path):
        file = open(model_path, 'rb')
        self.model = pickle.load(file)
        file.close()

        file = open(dictionary_path, 'rb')
        self.dic = pickle.load(file)
        file.close()

    def _lemmatize_stemming(self, text):
        stemmer = SnowballStemmer("english")
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    def _preprocess(self, text, min_length=3):
        if text is None:
            return []
        result=[]
        
        for token in gensim.utils.simple_preprocess(text, deacc=True) :
            # the follwing condition used to be > 3
            if token not in gensim.parsing.preprocessing.STOPWORDS and (len(token) > min_length):
                result.append(self._lemmatize_stemming(token))
    
        return result

    def findTopic(self, text):
        token = self._preprocess(text)

        bow_vector = self.dic.doc2bow(token)
        
        scores = []
        idx = []
        for index, score in self.model[bow_vector]:
            scores.append(score)
            idx.append(index)
        return (idx[np.argmax(scores)] + 1), float(0.01 * int(100 * np.amax(scores)))


    


    