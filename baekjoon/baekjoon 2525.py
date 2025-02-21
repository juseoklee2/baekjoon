#Hour is A, minute is B, and baking time is C.
A, B = map(int, input().split())
C = int(input())
# sum C on B
B += C
#As we did on last question, make a time adjustmemt.
#In this case, 'while'is effective. It continuously adjust the numbers to prevent B remaining more than 60.
while B >= 60:
    A += 1
    B -= 60

while B < 0:
    A -= 1
    B += 60
# We can use 'while' on A, but using % will be more effective.
# % results modulo, so if A goes above 24, it makes an adjustment easily.
A %= 24  

print(A, B)
