my_day= raw_input ("What day is it?")
my_vacation = raw_input ("Are you on vacation? (True or False)")


def alarm_clock(day,vacation):
	if vacation == True :
		return "off"
	elif day > 0 and day <6 and day != 's' :
		return "7:00"
	else: 
		return "10:00"

print alarm_clock (my_day, my_vacation)



		#Tues, not on vacation
print alarm_clock (2, False)
	#Sunday, on vacation
print alarm_clock (0,True)
	#Fri
print alarm_clock (5,False)	
print alarm_clock (6,False)	
print alarm_clock (1,False)
print alarm_clock ("s",True)	