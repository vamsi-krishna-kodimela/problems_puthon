def gcd(a, b):
    if(a == b):
        return a

    return gcd(a-b, b) if a > b else gcd(a, b-a)

print(gcd(4,2))