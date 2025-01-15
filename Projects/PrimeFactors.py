import math

def countOccurrence(a):
  k = {}
  for j in a:
    if j in k:
      k[j] +=1
    else:
      k[j] =1
  return k

def primeFactors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1,2):
        while n % i ==0:
            primes.append(i),
            n = n / i

    
    if not primes:
        return n
    return countOccurrence(primes)
    


print(primeFactors(2162160))