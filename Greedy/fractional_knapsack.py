n, W = map(int, input().split())
weight =[]
values =[]

for i in range(n):
    a,b = map(int,input().split())
    weight.append(a)
    values.append(b)


def knapsack(n,W,weight,values):
    A = [values[i]/weight[i] for i in range(n)]
    v = 0

    while n>0:
        i = 0
        if W == 0:
            return v
        i = A.index(max(A))
        a = min(weight[i],W)

        v = v+(a*(A[i]))
        weight[i]=weight[i]-a
        W = W-a
        n=n-1
        A.remove(max(A))

    return v


print(knapsack(n,W,weight,values))
