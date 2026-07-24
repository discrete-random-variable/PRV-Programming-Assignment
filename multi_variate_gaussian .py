import numpy as np
import matplotlib.pyplot as plt

def samples(n, N):
    U1 = np.random.rand(N,n)
    U2 = np.random.rand(N,n) # generate array of N*n where each colm is a vector X n = 10**5

    #box muller transform
    Z1 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
   # Z2 = np.sqrt(-2 * np.log(U2)) * np.sin(2 * np.pi * U1), Z1 Z2 follow normal 0-1 , np applies each operation elementwise, so only Z1 is enough
    return Z1

def generate_Y(A,b,X):
    return A @ X + b # python handels order 

def ecdf(data):
    x = np.sort(data)
    n = len(data)
    y = np.arange(1,n+1) / n
    return x,y

def mse(A,b,N):
    n_value = [10, 100, 1000, 10000, 10**5, 10**6]
    mse_value = []
    kactual = A @ A.T
    for n in n_value :
        X_sample = samples(n,N)
        Y_sample = generate_Y(A,b,X_sample)
        kemp = np.cov(Y_sample)
        mse = np.mean((kemp - kactual)**2)
        mse_value.append(mse)

    plt.plot(n_value, mse_value, marker = '+')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.xlabel("n values")
    plt.ylabel("mse values")
    plt.show()


# how to take input ?

N = 3
X = samples(10**5, N) 
#example
A = np.random.rand(3,3)
b = np.random.rand(3,1)
Y = generate_Y(A,b,X) # each colm is Y

#5.3 eg let i be 1
i = 1

Y_samples = Y[i, :]
x_Y, y_Y = ecdf(Y_samples)

# Gaussiann parameters
mu = b[i,0]
var = np.sum(A[i, :]**2)

U1new = np.random.rand(10**5)
U2new = np.random.rand(10**5)
Gauss_samples = (np.sqrt(-2 * np.log(U1new)) * np.cos(2 * np.pi * U2new)) * np.sqrt(var) + mu


x_G, y_G = ecdf(Gauss_samples)

plt.plot(x_Y, y_Y, label = 'Ecdf of Yi' )
plt.plot(x_G, y_G, label = 'Appropriate Gaussian', linestyle='--' )
plt.title(f'Comparision for index {i}')
plt.legend()
plt.show()

Kemp = np.cov(Y)
Kactual = A @ A.T

mse(A,b,N)
