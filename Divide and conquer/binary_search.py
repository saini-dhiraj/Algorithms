# python3
list_1 = [int(x) for x in input().split()]
list_2 = [int(x) for x in input().split()]

n = list_1[0]
array = list_1[1:]
m = list_2[0]
query = list_2[1:]

def binarysearch(A,k,beg,end):

    while(beg<=end):
        mid = int((beg + end) / 2)
        if A[mid] ==k:
            return mid
        elif A[mid]<k:
            beg =mid+1
        else:
            end = mid-1

    return -1

for k in query:
    print(binarysearch(array,k,0,n-1),end=' ')
