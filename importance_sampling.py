import numpy as np
import matplotlib.pyplot as plt

def generate_standard_gauss(n):
    U1 = np.random.rand(n)
    U2 = np.random.rand(n)
    Z1 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    return Z1

def emp_P(X):
    return np.mean(X > 4)

def P_IS(X):
    W = np.exp(8 - 4 * X)
    return np.mean((X > 4) * W), (np.sum((X > 4) * W) / np.sum(X > 4))



X = generate_standard_gauss(10**6)
print(emp_P(X))

Y = generate_standard_gauss(10**6) + 4

P,average_value = P_IS(Y)

print("Numerical value of P_IS ", P)
print("Average value of Importance weights over rare samples ", average_value)

N_trial = 10**6
MCE = [] #monte carlo estimator values
PIS = [] #importance sampling estimator values

for i in range(20):
    X = generate_standard_gauss(N_trial)
    MCE.append(emp_P(X))

    Y = generate_standard_gauss(N_trial) + 4
    a,b = P_IS(Y)
    PIS.append(a)

mc_mean = np.mean(MCE)
mc_var  = np.var(MCE, ddof = 1) # ddof tells python to devide by N - 1 for sample variance

is_mean = np.mean(PIS)
is_var  = np.var(PIS, ddof = 1)

print("Monte carlo sample")
print(f"mean {mc_mean}")
print(f"variance {mc_var}")

print("Importance Sampling sample")
print(f"mean {is_mean}")
print(f"variance {is_var}") # this var is 10000 time smaller than monte carlo , so this is better
