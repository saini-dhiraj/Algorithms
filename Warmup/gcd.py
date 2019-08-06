# python3

a,b = map(int,input().split())


def gcd(a, b):
    if b == 0 :
        return a
    c = a % b
    return gcd(b, c)


print(gcd(a,b))