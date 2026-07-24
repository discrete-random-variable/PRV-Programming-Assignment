import numpy as np
import matplotlib.pyplot as plt

def fair_coin():
    U = np.random.rand()
    if U >= 0.5 :
        return 1
    else:
        return 0
    
def biased_coin(p):
    current_p = p
    while(True) :
        current_p *= 2
        if current_p >= 1:
            b_k = 1
            current_p -= 1
        else:
            b_k = 0

        c_k = fair_coin()
        if c_k < b_k:
            return 1
        if c_k > b_k :
            return 0