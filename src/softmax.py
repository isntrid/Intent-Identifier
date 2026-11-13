import torch

def softmax(tensor):
    numerator = torch.exp(tensor)
    denominator = torch.sum(torch.exp(tensor))
    return numerator / denominator