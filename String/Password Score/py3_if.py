s=list(input())
score_pass=0
if len(s)<=4:
    score_pass+=5
elif len(s)>=5 and len(s)<=7:
    score_pass+=10
else:
    score_pass+=25

flag1_1=flag1_2=cou2=cou3=0
for i in range(len(s)):
    x=ord(s[i])
    if x<=122 and x>=97:
        flag1_1=1
    elif x<=90 and x>=65:
        flag1_2=1
    elif x<=57 and x>=48:
        cou2+=1
    else:
        cou3+=1

if flag1_1==1 and flag1_2==0:
    score_pass+=10
elif flag1_1==0 and flag1_2==1:
    score_pass+=10
elif flag1_1==1 and flag1_2==1:
    score_pass+=20

if cou2==1:
    score_pass+=10
elif cou2>1:
    score_pass+=20

if cou3==1:
    score_pass+=10
elif cou3>1:
    score_pass+=25

if cou2>=1:
    if cou3>=1:
        if flag1_1==1 and flag1_2==1:
             score_pass+=5
        elif flag1_1==1 or flag1_2==1:
            score_pass+=3
    elif flag1_1==1 or flag1_2==1:
        score_pass+=2

if score_pass>=90:
    result='VERY_SECURE'
elif score_pass<90 and score_pass>=80:
    result='SECURE'
elif score_pass<80 and score_pass>=70:
    result='VERY_STRONG'
elif score_pass<70 and score_pass>=60:
    result='STRONG'
elif score_pass<60 and score_pass>=50:
    result='AVERAGE'
elif score_pass<50 and score_pass>=25:
    result='WEAK'
elif score_pass<25:
    result='VERY_WEAK'
print(result)
