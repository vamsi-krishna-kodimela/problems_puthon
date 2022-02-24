def pow(a,x):
    if(x==1):
        return a
    return a*pow(a,x-1)
print(pow(10,3))