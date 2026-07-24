import numpy as np
import matplotlib.pyplot as plt

def inverse_cdf(n):
    U = np.random.rand(n)
    return -1 * np.log(1 - U)

def ecdf(data):
    x = np.sort(data)
    n = len(data)
    y = np.arange(1, n + 1) / n
    return x,y

def rejection_sampling(n):
    
    target = n
    count = 0
    proposal_count = 0
    accepted = []
    while count != target :
        proposal = inverse_cdf(1)[0]
        proposal_count = proposal_count + 1
        U = np.random.rand()
        if U <= 1 - np.exp(-2 * proposal):
            accepted.append(proposal)
            count = count + 1

    return accepted, proposal_count



N_samples = 10**5

sample = inverse_cdf(N_samples)
x_e, y_e = ecdf(sample)

MAX = max(sample)
x_thy = np.linspace(0,MAX,1000)
y_thy = 1 - np.exp(-1 * x_thy)


plt.plot(x_thy, y_thy, label = 'thy cdf')
plt.plot(x_e, y_e, label = 'ecdf', linestyle = '--')
plt.ylabel('CDF')
plt.title('Comparision')
plt.legend()
plt.show()


accepted_samples, proposal_number = rejection_sampling(10**5)
mu  = np.mean(accepted_samples)
var = np.var(accepted_samples)
accept_rate = len(accepted_samples) / proposal_number
print('emean', mu)
print('evar', var)
print('arate', accept_rate)

plt.hist(accepted_samples, bins = 100, density = True, alpha = 0.6, label = 'Empirical Histogram')

MAX = max(accepted_samples)
x_d = np.linspace(0,MAX,1000)
y_d = 1.5 * (np.exp(-x_d) - np.exp(-3 * x_d))

plt.plot(x_d, y_d, label = 'PDF' )
plt.xlabel('X values')
plt.ylabel('Density values')
plt.title('Comparision of theoritical density with generated from reduction sampling')
plt.legend()
plt.show()



