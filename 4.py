import numpy as np
import matplotlib.pyplot as plt

def generate_exp(n):
    U = np.random.rand(n)
    return -np.log(1-U)

def generate_2U(n):
    U = np.random.rand(n)
    return 2*U

def generate_PMF():
    U = np.random.rand()
    if U < 0.4 :
        return 1
    if 0.4 < U < 0.7 :
        return 2
    if 0.7 < U < 0.9 :
        return 3
    if U > 0.9 :
        return 4
    
def sample_mean_ecdf(N_size,m):
    # use function whichever needed
    #------------------------------------------- only for pmf, for given pdfs can directly use line in question 5
    samples = []
    for i in range(m): # loop 10**5 times
        PMF_samples = []
        for j in range(N_size):
            PMF_samples.append(generate_PMF())
            
        mean = np.mean(PMF_samples) # take average of samples
        samples.append(mean)
    #-------------------------------------------
    x = np.sort(samples)
    y = np.arange(1, m + 1) / m
    return x,y

def gaussian_ecdf(mu,var,N,n):
    U1 = np.random.rand(n)
    U2 = np.random.rand(n)
    sample_gauss = (np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2 )) * np.sqrt(var / N) + mu # from 4.3 mean is mu and variance is var/N 
    x = np.sort(sample_gauss)
    y = np.arange(1, n + 1) / n
    return x,y

# for given pmf
mu = 2
var = 1

N_trial = 10**5 # number of samples you want for 4.4
N_size = 50 # from 4.2 

x_mean, y_mean = sample_mean_ecdf(N_size,N_trial)
x_gauss, y_gauss = gaussian_ecdf(mu,var,N_size,N_trial)

plt.plot(x_mean, y_mean, label = 'emperical cdf of sample mean')
plt.plot(x_gauss, y_gauss, label = 'gaussian cdf with parameters', linestyle = '--')
plt.title('Comparision')
plt.legend()
plt.show()


