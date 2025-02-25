#Receive the word and i(functioned as finding the position of 'S')
S = input()
i = int(input())
# We can use '[]' to know the exact position.
# Python program always start with 0, so if we want to count as usual, subtract one.
w = S[i-1]
print(w)
