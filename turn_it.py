T = int(input())
for i in range(T):
    u, v, a, s = map(int, input().split())
    if(u**2-(2*a*s) <= v**2):
        print("Yes")
    else:
        print("No")
