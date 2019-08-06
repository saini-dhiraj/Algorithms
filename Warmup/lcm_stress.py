# python3
#a, b = map(int,input().split())

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


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


from random import randint

def stress(N):
    while True:
        n = randint(2,N)
        m = randint(2,N)
        #A = [None]*n
        #for i in range(n):
            #A[i] = randint(0,M)
        print(n,m)

        res1 = lcm(n,m)
        res2 = lcm_naive(n,m)

        if res1 == res2:
            print('ok')
        else:
            print('Wrong answer:', res1,res2)
            return

stress(100)