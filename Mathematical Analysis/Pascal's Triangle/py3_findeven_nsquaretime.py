import sys

n=int(input())
result=[[0]*n]*2
# print(result[0][0])
for i in range(n):
    for j in range(i+1):
        if j==0:
            if i==0:
                result[1][0]=1
            else:
                # print(i,result[0])
                result[1][0]=result[0][0]+2*result[0][1]
        elif j==i:
            result[1][j]=1
        else:
            result[1][j]=result[0][j-1]+result[0][j]+result[0][j+1]
    result[0]=result[1]
    result[1]=[0]*n

fl=-1
for i in range(n-1,-1,-1):
    if result[0][i]%2==0:
        fl=n-i
        break
print(fl)
