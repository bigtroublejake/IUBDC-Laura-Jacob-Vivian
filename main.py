# Could not figure out how to "properly" import the vaderSentiment module, so instead I just stuck it inside the project file and it works fine... so yeah
# https://github.com/cjhutto/vaderSentiment

# Note to myself while building this:
# Use the Anaconda interpreter, as that's the only one that seems to allow me to import pandas. Also run it in the terminal.
# No clue why it's like this, but it works so don't question it lol

from vaderSentiment import vaderSentiment as vs
import pandas as pd

# test to see if it imported correctly & is working
# print(vs.SentimentIntensityAnalyzer().polarity_scores("vader is dumb"))

testSentence = "vader is dumb"
# score = vs.SentimentIntensityAnalyzer().polarity_scores(testSentence)
# print(score["compound"])

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
    
# print(PosTest(testSentence))

testFileDep = pd.read_csv('Test Tweets/dataset_16_emojifinal.csv', usecols=['Text', 'Sentiment'])
# print(testFileDep.iterrows)

tweetList = []
correctPos = 0
incorrectPos = 0
correctNeg = 0
incorrectNeg = 0

for index, rows in testFileDep.iterrows():
    list = rows.Text

    # tweetList.append(str(list))
    result = PosTest(list)

    # Positive emotions
    if result == True and (rows.Sentiment == 1 or rows.Sentiment == 3):
        correctPos += 1
        print(index, 'C pos')
    # Negative emotions
    elif result == False and (rows.Sentiment == 0 or rows.Sentiment == 2):
        correctNeg += 1
        print(index, "C neg")
    # Wrong guess or netural emotion
    else:
        if rows.Sentiment == 1 or rows.Sentiment == 3:
            incorrectPos += 1
            print(index, 'I pos')
        elif rows.Sentiment == 0 or rows.Sentiment == 2:
            incorrectNeg += 1
            print(index, 'I neg')

    # print(list)

print(correctPos, incorrectPos, correctNeg, incorrectNeg, (correctPos+correctNeg)*100/(correctPos+incorrectPos+correctNeg+incorrectNeg))


# correctAssesments = 0
# for i in range(0,len(tweetList)):
#     result = PosTest(tweetList[i])
#     if result == False:
#         correctAssesments += 1
#         print("right", i)
#     else:
#         print ("wrong", i)

# print(correctAssesments, correctAssesments/len(tweetList)*100)





