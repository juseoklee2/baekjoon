H,M = map(int,input().split())
# First, subtract 45 from the minutes.
M -= 45
# What we need to focus on is the maximum of hour and minutes.
# If minute goes below 0, subtract 1 hour and add 60 on minutes.
if M < 0:
  H -= 1
  M += 60
# If Hour goes below 0, it has to be reset to 24.
if H < 0:
  H += 24
  

print(H, M )
