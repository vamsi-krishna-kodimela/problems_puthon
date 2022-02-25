T = int(input())
for i in range(T):
    n = int(input())
    s = 0
    for i in range(1, n+1):
        if(i == n):
            x = n-(s % 3)
            while(True):
                if(x % 2 != 0):
                    if((x+s) % 3 == 0 and (x+s) % 9 != 0):
                        break
                else:
                    x += 1
                x += 2
            s += x
        else:
            s += (i*(10**(n-i)))
    print(s)
