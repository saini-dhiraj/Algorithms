# python3

#### This is hard problem do research on it
def fibonacci_number_again_naive(n, m):

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    r = n%m
    f = []
    f.append(0)
    f.append(1)
    for i in range(2,r+1):
        f.append(f[i-1]+f[i-2])

    return f[r]%m


from random import randint

def stress(N):
    while True:
        n = randint(2,N)
        m = randint(2,N)
        print('n = ',n,' , m = ',m )

        res1= fibonacci_number_again_naive(n,m)
        res2= fibonacci_number_again(n,m)

        if res1 == res2:
            print('ok')
        else:
            print('wrong:',res1,res2)
            return

stress(10)