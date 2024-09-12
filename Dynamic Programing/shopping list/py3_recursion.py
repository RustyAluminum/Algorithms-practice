import sys
def plan_cycle(pi, ml, dgr_stfy, max_dgr_stfy):
    global pm
    global pp_info
    ml1 = ml - pp_info[pi][0]
    dgr_stfy1 = dgr_stfy + pp_info[pi][0] * pp_info[pi][1]
    pmain = pp_info[pi][2]
    pmain_info=pp_info[pmain - 1]
    pp_info_index=[]
    lg=0
    if pmain != 0:
        ml1 = ml1 - pp_info[pmain - 1][0]
        dgr_stfy1 = dgr_stfy1+pp_info[pmain-1][0] * pp_info[pmain-1][1]

    if ml1 > 0 and pi < pm - 1:
        dgr_stfy = dgr_stfy1
        ml = ml1
        if pmain != 0:
            pp_info_index.append(pmain-1)
            for i in range(pm):
                if pp_info[i][2] == pmain:
                    pp_info_index.append(i)
                    pp_info[i][2] = 0
            
            pp_info[pmain - 1]=[0,0,0]
        elif pmain == 0:
            for i in range(pm):
                if pp_info[i][2] == pi+1:
                    pp_info_index.append(i)
                    lg=1
                    pp_info[i][2] = 0
                
        for i in range(pi + 1, pm):
            max_dgr_stfy = plan_cycle(i, ml, dgr_stfy, max_dgr_stfy)
                    
    elif ml1 > 0 and pi == pm - 1:
        dgr_stfy = dgr_stfy1
        ml = ml1
    elif ml1 == 0:
        dgr_stfy = dgr_stfy1
        ml = ml1
    elif ml1 < 0:
        if pmain != 0:
            pp_info[pi][2]=pmain
            for i in pp_info_index:
                pp_info[i][2] = pmain
            pp_info[pmain - 1]=pmain_info
        elif lg==1:
            for i in pp_info_index:
                pp_info[i][2] = pi+1
        return max_dgr_stfy
    
    if pmain != 0:
        pp_info[pi][2]=pmain
        for i in pp_info_index:
            pp_info[i][2] = pmain
        pp_info[pmain - 1]=pmain_info
    elif lg==1:
        for i in pp_info_index:
            pp_info[i][2] = pi+1
    if dgr_stfy > max_dgr_stfy:
            max_dgr_stfy = dgr_stfy
    return max_dgr_stfy

line = sys.stdin.readline()
a = line.split()
N = int(a[0])
pm = int(a[1])
p_info = [[0] * 3] * pm
for i in range(pm):
    line = sys.stdin.readline()
    a = line.split()
    p_info[i] = [int(a[0]), int(a[1]), int(a[2])]

max_dgr_stfy = 0
for i in range(pm):
    ml = N
    dgr_stfy = 0
    pp_info = []
    for element in p_info:
        pp_info.append(element)
    max_dgr_stfy = plan_cycle(i, ml, dgr_stfy, max_dgr_stfy)
print(max_dgr_stfy)
