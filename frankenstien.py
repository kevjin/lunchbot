#monster is a boolean variable that is based upon whether the monster shows up or not
if(monster): #when the monster comes into play in the story.
	victor = "overcome with fear and anxiety"
	if(victor is afraid):
		monster_companion = False #victor destroys the monster companion creation
		monster=revengeful #monster becomes focused on revenge
elif(no_monster):
	if(pastoral):
		victor = "calm, critical thinking" #that's his usual behavior when alone or with henry or elizabeth
		if(in_the_boat):
			victor = "contemplating his meaning and value in life" #while in the boat, alone
		if(victor+elizabeth):
			victor = "worried constantly because of the monster" #victor is in a quandary of whether to tell lizzy or not
		if(victor+father):
			victor = "overjoyed, finds comfort" #loving father
	elif(urban):
		victor = "tries to fit in, continue a lovely life with his family" #he can't be a normal guy because the shadow of the monster fills him with anxiety and fear
		if(victor+villagers):
			society = "chaotic" #the villagers thinking he murdered Henry and bombast him
if(wedding_happens and monster_companion=False and monster=revengeful):
	elizabeth = False #monster kills elizabeth because Victor basically killed his companion
	victor=revengeful #victor becomes focused on revenge just like the monster
if(monster = victor): #both of them are focused on revenge
	monster_location, victor_location = "Arctic" #the arctic really mirrors their icy, vengeful hearts
	if(victor="dead"):
		monster = "sorrowful, regretful, and suicides" #no longer vengeful

print 'The End' #story ends
