import string
from dataset import load_dataset
vocabulary = []
dataset = load_dataset()

def tokenize(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    tokens = sentence.split()

    return tokens

def create_vocab(dataset):
    vocab = {
        word
        for sentence in dataset["text"]
        for word in tokenize(sentence)
    }
    
    return sorted(vocab)

def vectorize(sentence, vocab):
    vector = []
    tokens = tokenize(sentence)

    for word in vocab:
        if word in tokens:
            vector.append(1)
        else:
            vector.append(0)

    return vector


print(vectorize("you're brilliant honestly", create_vocab(dataset)))
