import numpy as np
import matplotlib.pyplot as plt
STARTING_COLOR="0" #if higher than 255, return to 0 and start again TO ADD SPACE, I COULD TURN THE REPITIONS INTO FUNCTIONS AND MAKE THE CODE NEATER
#Destroy arrays with less than x pixels
#look up down left right
#use recursion for method, sort of like zombie infection adjacent pixels
#autogenerate arrays and record the number, turn these arrays into images
#zombified pixels can only be zombified once, not twice or more
MAX_HORIZONTAL=640
MAX_VERTICAL=480
current_threshold = 0
THRESHOLD=10
rel_up = 10000 #relative MAXIMUM values to be changed with every loop, finds max parameters for surface to acqure crop section
rel_down = 0
rel_left = 10000  #make BIG values because you want to find less than numbers
rel_right = 0
not_edge=true
stepBack=true #STEP BACK IS TO PREVENT TARGET POINT FROM ALTERNATING BETWEEN LEFT AND RIGHT
x=0 #I NEED ALL 4 VALUES SO I CAN FIND THE LARGEST DIAGONAL AND USE THOSE TWO VALUES
y=0 #I need to write functions to control all this logic SGO LEFT IS THE DEFAULT LAST RESORT, AFTER CANNOT PROGRESS ANYMORE STEPS, START GOING UP WITH THE SAME LOGIC
repeats=0
while (not_edge): #keeps looping while the current target is not an edge
	if(image[x,y]-image[x+1,y]<THRESHOLD and stepBack and switch==0): #try going right
		x=x+1		#so x will always be one step behind it
		if(x>rel_right):
			rel_right=x
	elif(image[x,y]-image[x,y+1]<THRESHOLD): #try going down
		y=y+1	#so x will always be one step behind it
		if(x>rel_down):
			rel_down=y
			stepBack=true
	elif(image[x,y]-image[x-1,y]<THRESHOLD): #try going left MAKE A COMMAND TO NOT GO BACK TO PREVIOUS SQUARE	             MAYBE I SHOULD SWITCH TO USING CASES SO I CAN FIT IN 3 AND OPERATORS
		x=x-1
		if(x<rel_left):
			rel_left=x
			stepBack=false
	else:
		switch=1
		stepBack=true
	if(image[x,y]-image[x-1,y]<THRESHOLD and stepBack and switch==1): #try going right HONESTLY DONT THINK 3 AND OPERATORS WILL WORK TOGETHER LOL
		x=x-1		#so x will always be one step behind it
		if(x<rel_left):
			rel_left=x
	elif(image[x,y]-image[x,y-1]<THRESHOLD): #try going down
		y=y-1	#so x will always be one step behind it
		if(x<rel_up):
			rel_up=y
			stepBack=true
	elif(image[x,y]-image[x+1,y]<THRESHOLD): #try going left MAKE A COMMAND TO NOT GO BACK TO PREVIOUS SQUARE	
		x=x+1
		if(x>rel_right):
			rel_right=x
			stepBack=false
	else:
		if((rel_right-rel_left)*(rel_down-rel_up)>500) #500 is arbitrarily value, to determine whether size of area is warrant a search or not
			cv2.line(img,(rel_left, rel_up),(rel_right, rel_up),(255,0,0),5)
			cv2.line(img,(rel_left, rel_down),(rel_right, rel_down),(255,0,0),5)
			cv2.line(img,(rel_left, rel_up),(rel_left, rel_down),(255,0,0),5) #Blue Box
			cv2.line(img,(rel_right, rel_up),(rel_right, rel_down),(255,0,0),5)
			#RUN PYTESSER HERE>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<
		x=rel_right+1
		if(x>640): #Max horizontal pixel size
			x=0
			if repeats!=10: #we cant repeat over 480 pix because screen size is only 480 pix
				repeats++
			else:
				not_edge=false
		y=48*repeats
		rel_up = 10000 #RESESTTING THE VALUES FOR NEXT ITERATION-----------------------------------------------------------------
		rel_down = 0
		rel_left = 10000
		rel_right = 0
		stepBack=true
		#I DON"T KNOW IF I SHOULD BOTHER TO CHECK IF IT"S ON THE SAME POINT AS THE ORIGINAL, OR IF I SHOULD DRAW THE SQUARE NOW. I NEED A SQUARE ANYHOW TO FIND THE LARGEST DIAGONAL AND SET THAT AS MY TUPLE
for y in xrange(0,MAX_VERTICAL): #cycle through all y's I DONT THINK I NEED THIS STUFF BELOW -----------------------------------------------
	for x in xrange(0,MAX_HORIZONTAL): #cycle through all the x's
		if (image[x,y]): #check if already zombified
			pass
		else:
			if(image[x,y]-image[x,y+1]<THRESHOLD):
				add it to the array//
