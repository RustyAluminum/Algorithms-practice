n=int(input())
n_slfprt=0
a=[0,1,5,6]
for i in range(0,n+1):
    if i%10 in a:
        x=i
        isqure=x*x
        m=1
        while True:
            if (x-x%10)/10!=0:
                m+=1
                x=(x-x%10)/10
            else:
                break
        if (isqure-i)%(10**m)==0:
            n_slfprt+=1
print(n_slfprt)
