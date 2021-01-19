print("Enter the numbers")
num_arr = [ int(i) for i in input().split(",")]
s=''

for i in num_arr:
  s+=chr(64+i)
print(s)