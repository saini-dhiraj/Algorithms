# python3

n = int(input())

lst = [int(x) for x in input().split()]

index1 = 0
i = 1
while i < len(lst):
    if lst[i] > lst[index1]:
        index1 = i
    i = i + 1

index2 = 1 if index1 == 0 else 0

k = 0

while k < len(lst):
    if (lst[k] > lst[index2]) and (index1 != k):
        index2 = k
    k = k + 1

print(lst[index1]*lst[index2])