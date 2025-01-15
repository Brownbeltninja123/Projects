#1 + 2 + 3 + 4 + 5 + ... + n


#1
#1 + 2 -> 2 + FindSum(1)
#1 + 2 + 3 -> 3 + FindSum(2)
#1 + 2 + 3 + 4 -> 4 + FindSum(3)
#1 + 2 + 3 + n -> n + FindSum(n-1) 

#n * FindFactorial(n-1)

#fibbonachi(n) = fibbonachi(n-1) + fibbonachi (n-2)
#0 return 0

def Fibbonachi(n):
    if n == 0:
        return 0
    
    if ((n == 1) or (n==2)):
        return 1
    
    return (Fibbonachi(n-1) + Fibbonachi(n-2))

for i in range(1,100):
    print(Fibbonachi(i))