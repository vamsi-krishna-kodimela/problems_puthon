T = int(input())
for i in range(T):
    n = int(input())
    for i in range(1, n, 2):
        print(i+1, end=" ")
        print(i+2, end=" ")
    print(1, end="\n")
