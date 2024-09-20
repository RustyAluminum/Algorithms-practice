n=int(input())
ntri=n**3
nsqure=n**2
a=[]
if nsqure%2!=0:
    a.append(nsqure)
    x1=nsqure-2
    x2=nsqure+2
    for i in range(1,int((n+1)/2)):
        a.append(x1)
        a.append(x2)
        x1-=2
        x2+=2
else:
    x1=nsqure-1
    x2=nsqure+1
    a.append(x1)
    a.append(x2)
    for i in range(1,int(n/2)):
        x1-=2
        x2+=2
        a.append(x1)
        a.append(x2)

a.sort()
for i in range(len(a)):
    if i==n-1:
        print(a[i])
    else:
        print(a[i],end='+')
