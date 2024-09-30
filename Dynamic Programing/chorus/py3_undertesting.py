while True:
    try:
        N, N_height = int(input()), input().split()
        # N=6
        # N_height=[3,3,4,2,5,1]
        # for i in range(len(N_height)):
            # N_height[i] = int(N_height[i])
        Nout=N-1
        for i in range(1,N-1):
            j=i
            ## left min<--max
            nleft=0
            for j in range(i,0,-1):
                Nl=[]
                while 1:
                    j-=1
                    if N_height[j]<N_height[j+1]:
                        Nl.append(N_height[j])
                    if j==0:
                        break
                nleft=max(nleft,len(Nl))
            if nleft==0:
                continue

            ## right max-->min
            nright=0
            for j in range(i,N-1): 
                # print(j)
                Nr=[] 
                while 1:
                    j+=1
                    if N_height[j]<N_height[j-1]:
                        Nr.append(N_height[j])
                    if j==N-1:
                        break
                nright=max(nright,len(Nr))
                # print(Nr,nright,j)
            
            Nout=min(Nout,N-1-nright-nleft)
            # print(i,Nout)
            # exit()
            
        print(Nout)

    except:
        break
