n=int(input())
result=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if j==0:
            if i==0:
                result[i][j]=1
            else:
                result[i][j]=result[i-1][j]+2*result[i-1][j+1]
        elif j==i:
            result[i][j]=1
        else:
            result[i][j]=result[i-1][j-1]+result[i-1][j]+result[i-1][j+1]
            
