# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 01:14:55 2020

@author: hreef
"""
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob 


#function for image
def create_image(data, title="Image"):
    fig=plt.figure()
    fig.suptitle(title, fontsize=16)
    plt.imshow(data, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    return plt
#function for wordcloud data
def create_wordcloud(data):
    stopwords=set(STOPWORDS)
    #Appearance related
    wc = WordCloud(background_color="white", max_words = 30, stopwords = stopwords)
    wc.generate(data)
    return wc
#function for clearing punctuation
def punctuation_clean(data):
    
    for char in ",.'\n?":
        data=data.replace(char,'') 
    data= data.lower()
    word_list= data.split()
    print(word_list)
 #function for wordfrequency   
def wordfreq(data):
    d={}
    for word in word_list:
        d[word]= d.get(word,0)+1    
    d
#get highest to lowest sorted
    wordfreq = []
    for key, value in d.items():
        wordfreq.append((value,key))
    wordfreq
    wordfreq.sort(reverse=True)
    print(wordfreq)
    
df = pd.read_csv("../data/satisfaction.csv")
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',30)
pd.set_option('display.max_colwidth',1000)


"""QUESTION 2""" 
df['Question2']=df['Question2'].str.replace(",.'\n?","")
df['q2_vector'] = df['Question2'].apply(lambda x: x .replace(" to "," ").replace(" an ", " ").replace("those"," ").replace(" like "," ").replace(" i ", " ").replace(" on ", " ").replace(" of "," ").replace(" or ","").replace(" in ", "").replace(" and "," ").replace(" like "," ").replace(" all ","").replace(" their "," ").replace(" the "," ").replace(" with "," ").replace(" are "," ").replace(" of "," ").replace(" how "," ").replace(" why "," ").replace(" who "," ").replace(" have ", " ").replace(" is "," ").strip())
print(df['q2_vector'])
Q2 = str(df['q2_vector'])

pc=punctuation_clean(Q2)#PUNCTUATION CLEAN
pc
wf=wordfreq#WORD LIST
wc=create_wordcloud(Q2)#IMAGE CREATION
create_image(wc,'Who would benefit from this app?')

""" SPELLING CORRECTED Q2"""

checkedQ2 = TextBlob(Q2)
print("corrected text: "+str(checkedQ2.correct())) 
pc=punctuation_clean(str(checkedQ2))#PUNCTUATION CLEANING 
wf=wordfreq#WORD LIST
wc=create_wordcloud(str(checkedQ2))#WORD FREQ IMAGE
create_image(wc,'Who would benefit from this app?--spellchecked')

"""QUESTION 3""" 
df['Question3']=df['Question3'].str.replace(",.'\n?","")
print(df['Question3'])
df['q3_vector'] = df['Question3'].apply(lambda x: x .replace(" to "," ").replace(" an ", " ").replace(" for ", " ").replace(" of "," ").replace(" those"," ").replace(" like "," ").replace(" i ", " ").replace(" on ", " ").replace(" of "," ").replace(" or ","").replace(" in ", "").replace(" and "," ").replace(" like "," ").replace(" all ","").replace(" their "," ").replace(" the "," ").replace(" with "," ").replace(" are "," ").replace(" off "," ").replace(" how "," ").replace(" why "," ").replace(" who "," ").replace(" have ", " ").replace(" is "," ").strip())
print(df['q3_vector'])
Q3 = str(df['q3_vector'])
print(Q3)

pc=punctuation_clean(Q3)#PUNCTUATION CLEAN
wf=wordfreq#WORD LIST
wc=create_wordcloud(Q3)#Word cloud
create_image(wc,'What are the main benefits received from this app?')

"""SPELLING CORRECTED Q3"""

checkedQ3 = TextBlob(Q3)
print("corrected text: "+str(checkedQ3.correct())) 
pc=punctuation_clean(str(checkedQ3))#PUNCTUATION CLEAN
wf=wordfreq#WORD LIST
wc=create_wordcloud(str(checkedQ3))#WORD CLOUD
create_image(wc,'What are the main benefits received from this app?-spellchecked')


""" Question 4"""
df['Question4']=df['Question4'].str.replace(",.'\n?","")
print(df['Question4'])
df['q4_vector'] = df['Question4'].apply(lambda x: x .replace(" to "," ").replace(" an ", " ").replace(" for ", " ").replace(" of "," ").replace(" those"," ").replace(" like "," ").replace(" i ", " ").replace(" on ", " ").replace(" of "," ").replace(" or ","").replace(" in ", "").replace(" and "," ").replace(" like "," ").replace(" all ","").replace(" their "," ").replace(" the "," ").replace(" with "," ").replace(" are "," ").replace(" off "," ").replace(" how "," ").replace(" why "," ").replace(" who "," ").replace(" have ", " ").replace(" is "," ").strip())
print(df['q4_vector'])
Q4 = str(df['q4_vector'])
print(Q4)

pc=punctuation_clean(Q4)#PUNCTUATION CLEAN
wf=wordfreq#WORDLIST
wc=create_wordcloud(Q4)#Word cloud
create_image(wc,'How can we improve WILD AI')


"""SPELLING CORRECTED Q4"""

checkedQ4 = TextBlob(Q4)
print("corrected text: "+str(checkedQ4.correct())) 

pc=punctuation_clean(str(checkedQ4))#punctuation clean
wf=wordfreq#word list
wc=create_wordcloud(str(checkedQ4))#wordcloud
create_image(wc,'How can we improve WILD AI?-spellchecked')

