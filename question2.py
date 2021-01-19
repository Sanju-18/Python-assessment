# Getting values form the users.
# Enter the values seperated by space.
print("Enter the numbers")
num_arr = [int(i) for i in input().split(' ')]
sum_value = int(input("Enter the sum"))
length = len(num_arr)
flag =0

#Checking for the addition of pair of numbers equal to the given sum.
for i in range(length-1):
	for j in range(i+1, length):
		if num_arr[i]+num_arr[j] == sum_value:
			print(num_arr[i],num_arr[j])
			flag = 1

#Check whether no pair of number's addition equal to the given sum.
if flag==0:
	print("No pairs found");
