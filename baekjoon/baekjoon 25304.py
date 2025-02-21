#First, receive total costs and the number of items
X = int(input())
N = int(input())
#save values as "value"
value = []
#Receive the costs and number of items by 'a' and 'b'.
#After that, multiply them and save on 'value' to compare with X
for _ in range(N):
 a,b= map(int,input().split())
 value.append(a*b)
#lastly, compare those two values.
if sum(value) != X:
 print("No")
else:print("Yes")
