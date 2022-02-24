def prod(arr):
    if(len(arr)==1):
        return arr.pop()
    return arr.pop()*prod(arr)

print(prod([1,2,3,4,10]))