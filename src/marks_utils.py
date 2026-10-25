import numpy as np

def standardise_loop(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = variance ** 0.5
    return [(x - mean) / std for x in data]

def standardise_np(data):
    return (data - np.mean(data)) / np.std(data)