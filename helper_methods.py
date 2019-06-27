from random import randint
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def scale(number):
    if -1 <= number < -0.95:
        res = -1
    elif -0.95 <= number < -0.85:
        res = -0.9
    elif -0.85 <= number < -0.75:
        res = -0.8
    elif -0.75 <= number < -0.65:
        res = -0.7
    elif -0.65 <= number < -0.55:
        res = -0.6
    elif -0.55 <= number < -0.45:
        res = -0.5
    elif -0.45 <= number < -0.35:
        res = -0.4
    elif -0.35 <= number < -0.25:
        res = -0.3
    elif -0.25 <= number < -0.15:
        res = -0.2
    elif -0.15 <= number < -0.05:
        res = -0.1
    elif -0.05 <= number < 0.05:
        res = 0
    elif 0.05 <= number < 0.15:
        res = 0.1
    elif 0.15 <= number < 0.25:
        res = 0.2
    elif 0.25 <= number < 0.35:
        res = 0.3
    elif 0.35 <= number < 0.45:
        res = 0.4
    elif 0.45 <= number < 0.55:
        res = 0.5
    elif 0.55 <= number < 0.65:
        res = 0.6
    elif 0.65 <= number < 0.75:
        res = 0.7
    elif 0.75 <= number < 0.85:
        res = 0.8
    elif 0.85 <= number < 0.95:
        res = 0.9
    elif 0.95 <= number <= 1:
        res = 1
    else:
        raise ValueError("wrong input value")
    return res

def sentiment_score(inputStr):
    if inputStr is None:
        return 0
    vs = analyzer.polarity_scores(inputStr)
    number = 0.01 * int(100 * float(vs['compound']))
    number_scaled = scale(number)
    return number_scaled

