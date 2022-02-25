import math

T = int(input())
for i in range(T):
    n,k=map(int,input().split())
    p=1
    print(int(n/math.gcd(n,k)))