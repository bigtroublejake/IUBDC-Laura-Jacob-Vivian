# Could not figure out how to "properly" import the vaderSentiment module, so instead I just stuck it inside the project file and it works fine... so yeah
# https://github.com/cjhutto/vaderSentiment

# Note to myself while building this:
# Use the Anaconda interpreter, as that's the only one that seems to allow me to import pandas
# No clue why it's like this, but it works so don't question it lol

from vaderSentiment import vaderSentiment as vs
import pandas as pd

# test to see if it imported correctly & is working
# print(vs.SentimentIntensityAnalyzer().polarity_scores("vader is dumb"))

testSentence = "vader is dumb"
score = vs.SentimentIntensityAnalyzer().polarity_scores(testSentence)
print(score["compound"])

def PosTest(sentence):
    # running sentiment analysis
    score = vs.SentimentIntensityAnalyzer().polarity_scores(sentence)

    # positive
    if score["compound"] >= 0.05:
        return True
    # negative 
    elif score["compound"] <= -0.05:
        return False
    # neutral
    elif score["compound"] > -0.05 and score["compound"] < 0.05:
        return 
    
print(PosTest(testSentence))

