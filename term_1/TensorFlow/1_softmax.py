import numpy as np


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    expos     = np.exp(x)
    expos_sum = np.sum(expos)
    return (expos/expos_sum)

logits = [3.0, 1.0, 0.2]
print(softmax(logits))
