days_of_week = ['Sunday', 'monday', 'tuesday', 'wednesday','thursday','friday' , 'Saturday']

def prompt_user():
	return raw_input ('What is today?')

def display_tomorrow(today):
	tomorrow = (days_of_week .index(today)+ 1) % len(days_of_week)
	if tomorrow > 6: 
		tomorrow = 0
	print 'Tomorrow is', days_of_week[tomorrow]	

	def main():
		my_today = prompt_user()
		display_tomorrow(my_today)
		

if __name__ == '__main__':
	main ()



