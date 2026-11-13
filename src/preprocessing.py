import string
import torch
import re
from dataset import load_dataset


def tokenize(sentence):

    sentence = str(sentence)
    sentence = re.sub(r"[^a-zA-Z0-9\s.,!?'\-]", "", sentence)
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    tokens = sentence.split()
    
    return tokens

def create_vocab(dataset):
    vocab = {
        word
        for sentence in dataset["Comment"]
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

def tensorize(vector):
    tensor = torch.tensor(vector, dtype=torch.float32)
    return tensor


def process(sentence, vocab):
    vector = vectorize(sentence, vocab)
    tensor = tensorize(vector)
    return tensor