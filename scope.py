# scope_example
score = 0 --> Global

def increase_score(points):
	new_score = score + points 
	return new_score

print score
print new_score --> is tied to function and isn't defined


print score
print increase_score (10)
print score


IF YOU EVER WANT TO UPDATE PARAMETER USE GLOBAL IN FRONT OF IT




score = 0

def increase_score(points):
	global score
	score = score + points
	return score


print score
print increase_score(10)
print score


	



