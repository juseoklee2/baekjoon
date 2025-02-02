#First, receive two three-digit number.
one = int(input())
two = int(input())
#To solve this problem, we need each digit.
print(one * int(str(two)[2])) #int(str(two)[2]) will extract the digit in the one's place.
print(one * int(str(two)[1])) #int(str(two)[1]) will extract the digit in the ten's place.
print(one * int(str(two)[0])) #int(str(two)[0]) will extract the digit in the hundred's place.
print(one * two) # one * two will extract two three-digit number's multiplication.