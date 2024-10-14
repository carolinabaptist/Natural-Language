#How to tokenize a text using the `transformers` package ?

#Converter os tokens em uma forma numérica ou representá-los de maneira que possam ser processados por algoritmos de aprendizado de máquina
from transformers import AutoTokenizer

text="I love spring season. I go hiking with my friends"

#tokenizer
tokenizer=AutoTokenizer.from_pretrained('bert-base-uncased')
#words -> numbers
inputs=tokenizer.encode(text)
print(inputs)
#numbers -> words
decode = tokenizer.decode(inputs)
print(decode)
