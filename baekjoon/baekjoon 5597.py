#First, we need numbers from 1 to 30
stu = list(range(1,31))
#make a save space to compare numbers later.
num = []
#We need 28 numbers, so use 'for' and 'range'.
for _ in range(28):
  #use append and int(input)to save numbers that we received
  num.append(int(input()))
# In this case, we need to make those 'stu' and 'num' into a 'set'.
#The reason why making those into 'set' is because we need to compare those numbers so that we can find the missing ones.
stu_set = set(stu)
num_set = set(num)
#Find the missing number
ab = list(stu_set - num_set)
print(min(ab))
print(max(ab))
