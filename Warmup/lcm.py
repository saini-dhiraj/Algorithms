# python3
a, b = map(int,input().split())

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b == 0 :
        return a
    c = a % b
    return gcd(b, c)


def lcm(a,b):

    l=0
    if a> b:
        l = gcd(a,b)

    else:
        l = gcd(b,a)
    q=a*b
    return q//l

print(lcm(a,b))