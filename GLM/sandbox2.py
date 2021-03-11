import numpy as np
#from pylab import plt
import matplotlib.pyplot as plt

def dnorm(x, mu, sig):
    return 1/(sig * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sig**2))

def dexp(x, l):
    return l * np.exp(- l*x)

def like(parameters):
    [mu1, sig1, mu2, sig2] = parameters
    return dnorm(sample1, mu1, sig1).prod()*dnorm(sample2, mu2, sig2).prod()

def prior(parameters):
    [mu1, sig1, mu2, sig2] = parameters
    return dnorm(mu1, pooled.mean(), 1000*pooled.std()) * dnorm(mu2, pooled.mean(), 1000*pooled.std()) * dexp(sig1, 0.1) * dexp(sig2, 0.1)

def posterior(parameters):
    [mu1, sig1, mu2, sig2] = parameters
    return like([mu1, sig1, mu2, sig2])*prior([mu1, sig1, mu2, sig2])


#create samples
sample1 = np.random.normal(110, 3, 30)
print(sample1)
sample2 = np.random.normal(90, 7, 30)
print(sample2)


pooled= np.append(sample1, sample2)

plt.figure(0)
bins = np.arange(np.floor(np.min(pooled)), np.ceil(np.max(pooled))+1,1)
plt.hist(sample1,bins, alpha=0.5, edgecolor='k')
plt.hist(sample2,bins, alpha=0.5,  edgecolor='k')
plt.show()

mu1 = 100 
sig1 = 10
mu2 = 100
sig2 = 10
parameters = np.array([mu1, sig1, mu2, sig2])

niter = 10000

results = np.zeros([niter, 4])
results[1,:] = parameters

for iteration in np.arange(2,niter):
    candidate = parameters + np.random.normal(0,0.5,4)
    ratio = posterior(candidate)/posterior(parameters)
    if np.random.uniform() < ratio:
        parameters = candidate
    results[iteration,:] = parameters

#burn-in
results = results[499:niter-1,:]

mu1 = results[:,1]
mu2 = results[:,3]

plt.plot(results[:,1])
plt.plot(results[:,3])
plt.show()


d = (mu1 - mu2)
p_value = np.mean(d > 0)

plt.figure(1)
plt.hist(d)
plt.show()