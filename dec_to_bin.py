def conv(n):
    if(n == 0):
        return '0'
    return conv(n//2)+('0' if(n % 2 == 0) else '1')


print(conv(2))
