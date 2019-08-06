# python3

d = int(input())
limit = int(input())
n = int(input())
stops = [int(x) for x in input().split()]
stops.insert(0,0)
stops.append(d)

def minRefills(stops,n,limit):
    numRefills = 0
    currentRefills = 0

    while currentRefills <= n:
        lastRefills = currentRefills

        while(currentRefills <= n) & \
        ((stops[currentRefills+1]-stops[lastRefills])<= limit):

            currentRefills=currentRefills+1

        if currentRefills == lastRefills:
            return(-1)
        if currentRefills <=n:
            numRefills = numRefills+1

    return(numRefills)


print(minRefills(stops,n,limit))
