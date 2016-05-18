PI = 3.14159265359
RADIUS = 10

def circle_area():
	area = PI * (RADIUS **2)
	return area

def circle_diameter():	
	diameter= RADIUS * 2
	return diameter

def circle_circumference():
	circumference = 2 *PI * RADIUS
	return circumference



def main():
print "For Radius: ", RADIUS
print "The area is: ", circule_area()
print "The diameter is: ", circle_diameter()
print "The circumference is:", circle_circumference()

if __name__ == "__main__":
main()		