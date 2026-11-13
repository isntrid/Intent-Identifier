import torch

class IntentClassifier(torch.nn.Module):
    def __init__(self, vocab_length):
        super().__init__()
        self.layer = torch.nn.Linear(vocab_length, 3)