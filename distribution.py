#Author:Shreyas Mohan

import sys
import random
import math

#Seeding the random number generator
random.seed(0.3)
#Bernoulli Distribution
def bernoulli(nS,p):
	X = []
	p=float(p)
	if p < 0.0 or p > 1.0: sys.exit('Incorrect probability value : '+str(p))
	for i in range(nS):
		
		if random.random() <= p:
			X.append(1)
		else:
			X.append(0)
	return X
#Binomial Distribution
def binomial(nS,n,p):
	X = []
	p = float(p)
	if p < 0.0 or p > 1.0: sys.exit('Incorrect probability value : '+str(p))
	for i in range(nS):
		sum = 0
		for j in range(int(n)):
			
			if random.random() <= p:
				sum = sum + 1
		X.append(sum)
	return X
#Geometric Distribution
def geometric(nS, p):
	X = []
	p = float(p)	
	if p < 0.0 or p > 1.0: sys.exit('Incorrect probability value : '+str(p))

	for i in range(nS):
		trial = 1
		while random.random() > p:
			trial = trial + 1
		X.append(trial)
	return X
#Negative Binomial Distribution
def negBinomial(nS, k,p):
	X = []
	k = int(k)
	for i in range(nS):
		X.append(sum(geometric(k,p)))
	return X
#Poisson Distribution
def poisson(nS, lambd):
	X = []
	
	for i in range(nS):
		i = 0
		u = random.random()
		while u >= math.exp((0.0-float(lambd))):
			i = i + 1
			u = u * random.random()
		X.append(i)
	return X
#Arbitrary Discrete Distribution
def arbDiscrete(nS,args):
	X = []
	p = []
	for v in args:
		p.append(float(v))
	F = []
	for i in range(len(p)):
		F.append(sum(p[0:i+1]))
	if F[-1] != 1: sys.exit('Sum of probabilities should be equal to 1')
	for i in range(nS):
		t = 0
		u = random.random()
		while  F[t] <= u:
			t = t + 1
		X.append(t)
	return X
#Uniform Distribution
def uniform(nS, a,b):
	X = []
	a = float(a)
	b = float(b)
	if a>b:
		temp = a;
		a = b;
		b = temp;
	for i in range(nS):
		X.append(a+((b-a)*random.random()))
	return X
#Exponential Distribution
def exponential(nS, lambd):

	X = []
	for i in range(nS):
		X.append((0-(1/float(lambd)))*math.log(1-random.random()))
	return X
#Gamma Distribution
def gamma(nS, alpha, lambd):
	X = []
	for i in range(nS):
		X.append(sum(exponential(int(alpha),lambd)))
	return X
#Normal Distribution
def normal(nS,mu,sigma):
	X = []
	nS2 = int(math.ceil(float(nS)/2))
	mu = float(mu)
	sd = float(sigma)
	for i in range(nS2):
		u1 = random.random()
		u2 = random.random()
		z1 = math.sqrt((0-2)*math.log(u1))*math.cos(2*math.pi*u2)
		z2 = math.sqrt((0-2)*math.log(u1))*math.sin(2*math.pi*u2)
		X.append(mu + z1 * sd)
		X.append(mu + z1 * sd)
	if nS % 2 == 0:
		return X
	else:
		return X[0:len(X)-1]

def main(argv):
	samples=int(argv[1])
	distribution=argv[2].lower()

	if distribution=="bernoulli":
		result=bernoulli(samples,argv[3])
	elif distribution=="binomial":
		result=binomial(samples,argv[3],argv[4])
	elif distribution=="geometric":
		result=geometric(samples,argv[3])
	elif distribution=="neg-binomial":
		result=negBinomial(samples,argv[3],argv[4])
	elif distribution=="poisson":
		result=poisson(samples,argv[3])
	elif distribution=="arb-discrete":
		args = argv[3:len(argv)]
		result=arbDiscrete(samples,args)
	elif distribution=="uniform":
		result=uniform(samples,argv[3],argv[4])
	elif distribution=="exponential":
		result=exponential(samples,argv[3])
	elif distribution=="gamma":
		result=gamma(samples,argv[3],argv[4])
	elif distribution=="normal":
		result=normal(samples,argv[3],argv[4])
	else:
		print "Invalid Distribution"
	print 'Values: ' + str(result)


if __name__ == '__main__':
	main(sys.argv)
