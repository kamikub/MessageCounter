import numpy as np
import pandas as pd

f = open('whatsapp.txt', encoding='UTF-8')
count = 0
numlist  = []
for item in f:
    ismessage = item.find(' - ')
    if ismessage > -1:
        endNum = item.find(':',15)
        if endNum > -1:
            numlist.append(item[ismessage+3:endNum])
f.close()
NumCounts =pd.Series(np.array(numlist)).value_counts()
NumCounts.to_csv('out.csv', encoding='utf-8')
