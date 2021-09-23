import string
from collections import Counter
import matplotlib.pyplot as plt


#reading text file
text = open('read.txt',encoding='utf-8').read()

#converting to lowercase
lower_case = text.lower()

#Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


#Removing stop words from the tokenized words list
finalwords=[]
for word in tokenized_words :
    if word not in stop_words:
        finalwords.append(word)
#print(finalwords)


#1Check if the word in the final word list is also present in emotion.txt
emotion_list = []
with open('emotions.txt','r') as file :
    for line in file :
        #Remove New line\n comma , and single quote from text file and save in cleared_line
        cleared_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        #print(cleared_line)
        word , emotion = cleared_line.split(':')
        #print(word)
        #print(emotion)
        #print("word :"+word+" "+"emotion :"+emotion)

        #If word is present -> Add the emotion to emotion_list
        if word in finalwords :
             emotion_list.append(emotion)
print(emotion_list)

#count each emotion in the emotion list
w = Counter(emotion_list)
print(w)



# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
#plt.bar(w.keys(),w.values())
plt.xlabel('Emotions')
plt.ylabel('No of occurances')
plt.savefig('output.png')
plt.show()