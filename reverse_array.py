def rev(arr):
    if(len(arr) == 0):
        return
    print(arr.pop())
    rev(arr)


rev([1, 2, 3, 4, 5, 6])
