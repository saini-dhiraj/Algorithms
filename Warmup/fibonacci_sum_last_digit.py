# python3

n = int(input())

m = (n + 2) % 60
f = []
f.append(0)
f.append(1)
for i in range(2, m + 1):
    f.append(f[i - 1] + f[i - 2])


r = f[m] % 10
print (r - 1)
