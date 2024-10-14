#How to add custom stop words in spaCy ?
#Add the custom stopwords “NIL” and “JUNK” in spaCy and remove the stopwords in below text
import spacy
nlp=spacy.load("en_core_web_sm")

customize_stop_words = ['NIL','JUNK']
text=" Jonas was a JUNK great guy NIL Adam was evil NIL Martha JUNK was more of a fool "

for w in customize_stop_words:
    nlp.vocab[w].is_stop = True 

doc = nlp(text)
#Esse objeto Doc é uma estrutura de dados central no spaCy que contém a tokenização e todas as anotações feitas pelo modelo (como parte do discurso, entidades nomeadas, dependências sintáticas, etc.).

tokens = [token.text for token in doc if not token.is_stop]

result = " ".join(tokens)

print(result)
