lis = []
N = int(input())
se = list(map(int,input().split()))
k = max(se)
for num in se:
   z = num / k * 100
   lis.append(z)
total = sum(lis)
re = total / N
print(re)

   

    

