def evenSum(a,b):
    if(a>=b):
        return 0
    if(a%2==1):
        a+=1
    return a+evenSum(a+1,b)
print(evenSum(6,8))