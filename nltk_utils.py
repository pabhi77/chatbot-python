import nltk
#nltk.download('punkt')
#nltk.download('punkt_tab') 
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(all_words,tokenized_sentence):
    pass

# stringA="how long does shipping will take?"
# print(stringA)
# stringA=tokenize(stringA)
# print(stringA)
words=["Organize","organizes","organizing"]
stemmed_words=[stem(w)for w in words]
print(stemmed_words)