#How to tokenize a given text?

import nltk

nltk.download('punkt') #tokenizer
text="Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided."
tokens=nltk.word_tokenize(text)
for token in tokens:
  print(token)
