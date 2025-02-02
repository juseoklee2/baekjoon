'''
Problem: Write a program that compares two integers, A and B.

Input: On the first line, two integers A and B are given, separated by a space.

Output: Print one of the following three symbols:

If A is greater than B, print '>'.
If A is smaller than B, print '<'.
If A and B are equal, print '=='.
'''

A,B = map(int,input().split())
#To compare A and B, use "if"
if A > B:
  print(">")
#To handle other situations, use "elif".
elif A < B:
  print("<")
#To handle all cases that are not covered by "if" or "elif", use "else".
else: 
  print("==")