from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
analyzer = SentimentIntensityAnalyzer()


if __name__ == '__main__':
    string = sys.argv[1]  # getting the input string
    vs = analyzer.polarity_scores(string) # applying the sentiment analyzer
    number = 0.01 * int(100 * float(vs['compound']))
    print(str(number))