import string
def main():
	print "Should you eat Bacon?"

	input_1 = raw_input("Do you want to feel like angels are frolicking on your taste buds?")
	input_1 = string.upper(input_1)
	if input_1 == "YES":
		print "Eat it!"
	elif input_1 == "NO":
		print "You've clearly never tasted bacon!" 
		print "Eat it!!"
	elif input_1 == "YES, BUT BACON WILL KILL ME":
		input_2 = raw_input("Are you a coward?")
		input_2 = string.upper(input_2)
		if input_2 == "I AM NOT":
			print "Then eat it"
		elif input_2 == "YES, I AM A COWARD":
			print "Bacon will turn you into a true warrior"	


			

if __name__ == '__main__':
	main()


	