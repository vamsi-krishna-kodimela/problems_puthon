T = int(input())
for i in range(T):
    l, r = map(int, input().split())
    print(r*2-l*2+1)
