import math

def primes_sieve():
    limitn = limit+1
    not_prime = set()
    primes = []
    listLimit = set()
    

    for j in range(start, limitn):
        listLimit.add(j)

    print('Number in list', listLimit)

    
        
    count = 0
    for i in range(start, limitn):
        if i in not_prime:
            continue  #if i in not_prime go back to check condition again 
        
        for f in range(i*start, limitn, i):
            not_prime.add(f) 
        listLimit = listLimit - not_prime
            

        primes.append(i)

    #print(listStep)
        #print('not prime = ', not_prime)

        if math.pow(i, 2) < limit :
            print('                                    ')
            print('                                    ')
            print('step ',count ,' = ', listLimit)
            print('                                    ')
            print('                                    ')
            count = count + 1
        else:
            break
            
                
                
    
    
    
    

limit = int(input("What you limit : "))
start = int(input("What you need to start : "))
primes_sieve()
