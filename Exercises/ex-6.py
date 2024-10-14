#How to tokenize text with stopwords as delimiters?

#Tokenize the given text with stop words (“is”,”the”,”was”) as delimiters. 
#Tokenizing this way identifies meaningful phrases.

import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

text = "Walter was feeling anxious. He was diagnosed today. He probably is the best person I know."

stop_words_and_delims = ['was', 'is', 'the', '.', ',', '-', '!', '?']

# Substitui a stopword por 'DELIM'
for r in stop_words_and_delims:
    text = text.replace(r, 'DELIM')
#text -> Walter DELIM feeling anxiousDELIM He DELIM diagnosed todayDELIM He probably DELIM DELIM best person I knowDELIM

words = [t.strip() for t in text.split('DELIM')]
# text.split('DELIM') -> ['Walter ', ' feeling anxious', ' He ', ' diagnosed today', ' He probably ', ' ', ' best person I know', '']
#t.strip() removes blank space
# words -> ['Walter', 'feeling anxious', 'He', 'diagnosed today', 'He probably', '', 'best person I know', '']

words_filtered = list(filter(lambda a: a not in [''], words))
#Para cada elemento em words, se o valor de a não for uma string vazia (''), ele será mantido na nova lista.
print(words_filtered)
