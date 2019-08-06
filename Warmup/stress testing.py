from random import randint

def stress(N,M):
    while True:
        n = randint(2,N)
        A = [None]*n
        for i in range(n):
            A[i] = randint(0,M)
        print(A)

        res1 = funcA()
        res2 = func2()

        if res1 = res2:
            print(ok)
        else:
            print('Wrong answer:', res1,res2)
            return

