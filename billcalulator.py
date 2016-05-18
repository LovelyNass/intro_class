bill_amount = None
tip_amount = None

def calculate_tip(bill_amount, tip_percentage):
	return bill_amount * tip_percentage

def calculate_total_bill():
	return bill_amount + tip_amount	

print calculate_tip(100, 0.18)	
print calculate_total_bill ()


#2


global_bill_amount = int(raw_input("What is the bill amount?"))
tip_amount= None

def calculate_tip (bill_amount, tip_percentage):
	tip_percentage = float( raw_input ( " How much do you want to tip?"))
	return global_bill_amount * tip_percentage

def calculate_total_bill():
	global global_bill_amount
	global_bill_amount = global_bill_amount + tip_amount
		return global_bill_amount

def split_bill():
	number_of_people = int(raw_input( "How many people?"))
	return global_bill_amount / number_of_people 




tip_amount = calculate_tip()
print "Your tip amount is", total_tip
print  "Total Bill is", calculate_total_bill()
bill_per_person = split_bill()
print "Amount per person is", bill_per_person



