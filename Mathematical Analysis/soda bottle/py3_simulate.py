import sys

n=[]
while 1:
    a=int(input())
    if a==0:
        break
    n.append(a)

for i in range(len(n)):
    empty_bo=n[i]
    gain_bo=0
    while 1:
        if empty_bo>=3:
            empty_bo=empty_bo-3
            gain_bo+=1
            empty_bo+=1
        elif empty_bo==2:
            empty_bo+=1
        elif empty_bo<2:
            break
    print(gain_bo)
