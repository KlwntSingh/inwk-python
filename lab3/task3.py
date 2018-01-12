import math

def fact(k):
	if(k <= 1):
		return(1)
	return k * fact(k-1)

def estimate_pi():
	sum = 0;
	k=0
	terminating_val=10**-15
	while True:
		val=(fact(4*k) * (1103 + 26390 *k))/(fact(k)**4 * 396**(4*k))
		if(val<terminating_val):
			break
		sum+=val
		k+=1
	calculated_pi=1/(2*math.sqrt(2)/9801*sum)
	return (calculated_pi)


print(estimate_pi())
print(math.pi)

