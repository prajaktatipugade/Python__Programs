def prime_factor(n):
    prime = []
    for i in n:
        flag = 0
        if i==1:
            flag=1
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag ==0:
            prime.append(i)            
    return prime
