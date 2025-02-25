#First, receive N items of subjects
N = int(input())
#make a variable that contain scores
score = list(map(int,input().split()))[:N]
#biggest number will be 'big'
big = max(score)
#lastly, get a revised average.
total = sum(score)/big*100/N
print(total)
