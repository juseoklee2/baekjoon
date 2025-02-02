'''
Problem:

Multiplying two three-digit numbers involves the following steps:

When three-digit natural numbers are given for positions (1) and (2), the values for positions (3), (4), (5), and (6) need to be calculated.

Input:

The first line contains the three-digit natural number to be placed in position (1).
The second line contains the three-digit natural number to be placed in position (2).
Output:

Output the values for positions (3), (4), (5), and (6) in order:
(3) is the product of the one's place of the first number and the one's place of the second number,
(4) is the product of the ten's place of the first number and the one's place of the second number,
(5) is the product of the hundred's place of the first number and the one's place of the second number,
(6) is the final multiplication result of both numbers.
'''

#First, receive two three-digit number.
one = int(input())
two = int(input())
#To solve this problem, we need each digit.
print(one * int(str(two)[2])) #int(str(two)[2]) will extract the digit in the one's place.
print(one * int(str(two)[1])) #int(str(two)[1]) will extract the digit in the ten's place.
print(one * int(str(two)[0])) #int(str(two)[0]) will extract the digit in the hundred's place.
print(one * two) # one * two will extract two three-digit number's multiplication.
