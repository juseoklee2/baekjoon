#Receive the number of numbers and whole number without blank.
N = int(input())  
num_str = input() 
#int(digit) makes the numbers into a integar
#Using 'for digit in num_str' makes the program take one digit at a time from the string
total = sum(int(digit) for digit in num_str) 
print(total)  
