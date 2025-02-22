N = int(input())
# we need to receive 'N'items horizontally and also we're gonna use 'count', so they need to be changed to a 'list'.
M = list(map(int,input().split()))
V = int(input())
#'count' functioned as counting. 'count' counts how many times the nubmer appears
count = M.count(V)
print(count)
