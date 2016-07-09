STARTING_COLOR="0" #if higher than 255, return to 0 and start again
#Destroy arrays with less than x pixels
#look up down left right
#use recursion for method, sort of like zombie infection adjacent pixels
#autogenerate arrays and record the number, turn these arrays into images
#zombified pixels can only be zombified once, not twice or more
MAX_HORIZONTAL="i don't know yet"
MAX_VERTICAL="I don't know yet"
THRESHOLD=10
x=1
y=1
for y in xrange(1,MAX_VERTICAL):
	pass
	for x in xrange(1,MAX_HORIZONTAL):
		pass
		if(image[x,y]-image[x,y-1]<THRESHOLD):
			add it to the array
