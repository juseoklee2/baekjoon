T =int(input())
# To solve this problem, we have to save our values into "value"
value = []
#After that, we will receive numbers about 'T' times.
for _ in range(T):
  A,B = map(int,input().split())
  #We have to print those in the last step, so just append those "A + B" into "Value".
  value.append(A + B)
#To print them vertically, use a 'for' loop. It will print them one by one in a vertical way.
for val in value:
  print(val)
