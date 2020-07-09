import pandas as pd
import numpy as np
import os
import re
from datetime import datetime
import json

personName = " Jaba Dutta"

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
        listsent_i.append(listsent[i])
        listreceived_i=[]
        listreceived_i.append(listreceived[i])
        responseDictionary.update(patterns = listsent_i, responses = listreceived_i)
        finallist.append(responseDictionary)
        finalDictionary={"intents":finallist}       
    return finalDictionary

combinedDictionary = dict()
print ('Getting chat Data')
combinedDictionary.update(getData())
print ('Total len of dictionary', len(combinedDictionary))

print ('Saving conversation data dictionary')
np.save('conversationDictionary.npy', combinedDictionary)

with open('file.txt', 'w') as file:
     file.write(json.dumps(combinedDictionary))
