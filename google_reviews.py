#programme to read json file
import json
import regex

import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
import string
import re
import emoji
from pandas_profiling import ProfileReport



# open json file
f = open('google_reviews.json',"r")

# Return json object as a dictionary
data = json.load(f)

# iterating through the json list
# for i in data:
#    print(i)
# print(len(data))

df=pd.DataFrame(data)
prof = ProfileReport(df)
prof.to_file(output_file='output.html')
df=df[["reviewCreatedVersion", "score","content"]]

#Check for missing values
check_total_none=df.isnull().sum()
print(check_total_none)

# Check how many times score 5 and 3 is received
score_high= df[df["score"]==5]
print("score high:",score_high)
score_mid=df[df["score"]==3]
print("score_mid:",score_mid)

#Print all unique versions
print(df.reviewCreatedVersion.unique())
print(df.reviewCreatedVersion.nunique())

#groupby versions, find average rating

x=(df.groupby('reviewCreatedVersion')['score'].mean())
print(x)

#histogram to find which score is max and min.
plt.hist(df['score'], bins = 5)
plt.show()

# Lower casing
# Change the reviews type to string
df['content'] = df['content'].astype(str)

## Before lowercasing
print(df['content'][2])

#Lowercase all reviews
df['content']= df['content'].apply(lambda x: x.lower())
print(df['content'][2]) ## to see the difference

#special characters
#check if there is any special character
alphabet = string.ascii_letters+string.punctuation
print(df.content.str.strip(alphabet).astype(bool).any())

extracted_emojis=[]
def extract_emojis(s):
    expe = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    #return expe.findall(s)
    return expe.sub(r'',s)

for y in df['content']:
     #print(str(extract_emojis(y)))
     extracted_emojis.append(str(extract_emojis(y)))

#print(extracted_emojis)

# stop words
stop_words=stopwords.words('english')
df['extracted_emojis'] = extracted_emojis
df['extracted_emojis']= df['extracted_emojis'].apply(lambda x:x if x not in stop_words else None)
print(df['extracted_emojis'][5])

# stemming
def stemming(x):
    st = PorterStemmer()
    if x is not None:
        for word in x.split():
            st.stem(word)

df['extracted_emojis'].apply(lambda x:stemming(x))
print(df['extracted_emojis'][100])

#Function to calculate sentiment score for whole data set
def senti_sc(x):
    if x is not None:
        return TextBlob(x).sentiment

df["Sentiment_score"]= df["extracted_emojis"].apply(senti_sc)
print(df.Sentiment_score.head(50))
print(df.loc[0:19,['extracted_emojis','Sentiment_score']])



f.close()




