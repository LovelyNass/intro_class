#Create a function called sum_nums that takes in a number called num. 
# sum_nums should add up all of the numbers from 0 until 
# (but not including) num. sum_nums should return this sum.


# sum_nums(2)=1 
# sum_nums(5) 0+1+2+3+4=10

def sum_nums(num):
	# sum, initial = 0
	sum = 0
	# for each item in a list of nums [0, 1, 2, 3 ... num-1]
	for x in range(num):

		# add current item to the sum
		# iteration 1:
		# sum = 0
		# x = 0
		# sum = 0

		# iteration 2:
		# sum = 0
		# x = 1
		# sum = 1

		# iteration 3:
		# sum = 1
		# x = 2
		# sum = 3

		# iteration 4:
		# sum = 3
		# x = 3
		# sum = 6

		sum = x + sum 
	# return sum
	return sum

print sum_nums(3)
print sum_nums(4)




