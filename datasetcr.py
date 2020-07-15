import pandas as pd
import numpy as np
import os
import re
from datetime import datetime
import json

personName = " Jaba Dutta"

#The file must not contain more than one comma each row. if there is a comma in between text, it will throw an error.
#remove commas from text part to avoid errors.
def getData():
    df = pd.read_csv('whtc.csv')
    responseDictionary = dict()
    receivedMessages = df[df['From'] != personName]
    sentMessages = df[df['From'] == personName]
    listreceived = receivedMessages['Content'].values.tolist()
    listsent = sentMessages['Content'].values.tolist()
    finallist=[]        
    finalDictionary = {'intents':'demo'}
    for i in range (0,14):
        responseDictionary = {"tag":i}
        listsent_i=[]
        listsent_i.append(cleanText(listsent[i]))
        listreceived_i=[]
        listreceived_i.append(cleanText(listreceived[i]))
        responseDictionary.update(patterns = listsent_i, responses = listreceived_i)
        finallist.append(responseDictionary)
        finalDictionary={"intents":finallist}       
    return finalDictionary

def cleanText(Text):
    # Remove new lines within message
    cleanedText = Text.replace('\n',' ').lower()
    # Remove punctuation
    cleanedText = re.sub('([,])','', cleanedText)
    # Deal with some weird tokens
    cleanedText = cleanedText.replace("\xc2\xa0", "")
    # Remove multiple spaces in message
    cleanedText = re.sub(' +',' ', cleanedText)
    cleanedText = cleanedText.encode('ascii', 'ignore').decode('ascii')
    return cleanedText

combinedDictionary = dict()
print ('Getting chat Data')
combinedDictionary.update(getData())
print ('Total len of dictionary', len(combinedDictionary))

print ('Saving conversation data dictionary')
np.save('conversationDictionary.npy', combinedDictionary)

with open('file.json', 'w') as file:
     file.write(json.dumps(combinedDictionary))
