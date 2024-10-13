def en_num(x):
    num1 = ["zero","one","two","three","four","five","six","seven",
"eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    num2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    # num3 = ["hundred", "thousand", "billion", "million"]
    num_str=[]
    if x<20:
        print(num1[x])
        return
    elif x<100:
        num_str.append(num_ten(x))
    elif x<1000:
        x1=x//100
        num_str.append(num1[x1]+' hundred')
        x2=x%100
        if x2>0:
            num_str.append(' and'+num_ten(x2))
    elif x<1000000:
        x1=x//1000
        if x1>100:
            num_str.append(num1[x1//100]+' hundred'+' and')
        num_str.append(num_ten(x1%100)+' thousand')
        
        x2=x%1000
        if x2>=100:
            num_str.append(num1[x2//100]+' hundred')
            if x2%100>0:
                num_str.append('and '+num_ten(x2%100))
        else:
            num_str.append(num_ten(x2%100))
    else:
        x0=x//1000000
        num_str.append(num1[x0]+' million')
        x1=(x%1000000)//1000
        if x1>100:
            num_str.append(num1[x1//100]+' hundred'+' and')
        num_str.append(num_ten(x1%100)+' thousand')
        x2=x%1000
        if x2>100:
            num_str.append(num1[x2//100]+' hundred'+' and')
        num_str.append(num_ten(x2%100))
    
    print(' '.join(num_str))
    

def num_ten(x):
    num1 = [0,"one","two","three","four","five","six","seven",
"eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    num2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    if x<20:
        return num1[x]
    else:
        x1=x//10
        x2=x%10
        if x2>0:
            return num2[x1-2]+' '+num1[x2]
        else:
            return num2[x1-2]

while True:
    try:
        x = int(input())
        en_num(x)
    except:
        break
