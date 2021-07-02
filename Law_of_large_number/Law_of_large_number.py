#Generate a population of random numbers

import numpy as np
import matplotlib.pyplot as plt

population_size = 2.3e5

sample_size=50
number_of_samples=500

#Generate the population distribution
# a population of numbers that decreases with increasing value
population = 1 / np.logspace(np.log10(.001),np.log10(10),int(population_size))

#computer mean of population data
trueMean = np.mean(population)

plotskip = int(1e3)
plt.plot(population[::plotskip],'o')
plt.xlabel('Sample')
plt.ylabel('Data value')
plt.show()

# shuffle the data

np.random.shuffle(population)
plt.plot(population[::plotskip],'o')
plt.xlabel('Sample')
plt.ylabel('Data value')
plt.show

# generate one random from the population
randsample = np.random.choice(population, size=sample_size)
print(np.mean(randsample))

# Monte carlo sampling for sample means

samplemeans = np.zeros(number_of_samples)

for expi in range(number_of_samples):
	randsample = np.random.choice(population, size=sample_size)
	samplemeans[expi] = np.mean(randsample)

plt.plot(samplemeans, 'ko',markerfacecolor='k',label='sample means')
plt.plot([0,number_of_samples],[trueMean,trueMean],'r',linewidth=5,label='True mean')
plt.legend()
plt.xlabel('sample means')
plt.ylabel('Mean value')
plt.show()

#cumulative Averaging

cumave = np.zeros(number_of_samples)

for i in range(number_of_samples):
	cumave[i] = np.mean(samplemeans[:i])

print(cumave)	

#another method to find cumulative average without loops
cumaves = np.cumsum(samplemeans)/np.arange(1,number_of_samples+1)

plt.plot(cumave,'ko',label="cumulative averages")
plt.plot(cumaves,'b+',label='cumulative averages alternative')
plt.plot([0,number_of_samples],[trueMean,trueMean],'r',linewidth=5,label='True mean')
plt.xlabel('Sample number')
plt.ylabel('Mean value')

plt.legend()
plt.show()

# central limit theorem

plt.hist(samplemeans,bins='fd')
plt.xlabel('Sample mean')
plt.ylabel('Count')
plt.show() #will create a histogram