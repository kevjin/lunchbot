#!/usr/bin/env python

'''
Copyright (c) 2015, Mark Silliman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

# Monitor the netbook's battery level

import roslib
import rospy
from go_to_specific_point_on_map import GoToPose #for specific locations
from smart_battery_msgs.msg import SmartBatteryStatus #for netbook battery
from kobuki_msgs.msg import ButtonEvent

class netbook_battery():

	def __init__(self):
		rospy.init_node("netbook_battery")		

		#monitor netbook's battery status.  Everytime anything changes call the call back function self.NetbookPowerEventCallback and pass the data regarding the current battery status
		rospy.Subscriber("/laptop_charge/",SmartBatteryStatus,self.NetbookPowerEventCallback)

		#rospy.spin() tells the program to not exit until you press ctrl + c.  If this wasn't there... it'd subscribe to /laptop_charge/ then immediatly exit (therefore stop "listening" to the thread).
		rospy.spin();


	def NetbookPowerEventCallback(self,data):
		print("Percent: " + str(data.percentage)) 
		print("Charge: " + str(data.charge))
		if(int(data.charge_state) == 1):
			print("Currently charging")
		else:
			print("Not charging")
			if int(data.percentage) < 50:
				print("Going home")
				GoToPose(x1, y1)
			#Go back to charging station. Replace x and y arguments with first two pose coordinates seen on gmapping	
		print("-----")
		#Tip: try print(data) for a complete list of information available in the /laptop_charge/ thread

#if __name__ == '__main__':
#try:
#netbook_battery()
#except rospy.ROSInterruptException:
#rospy.loginfo("exception")

class kobuki_button():

	def __init__(self):
		rospy.init_node("kobuki_button")		

		#monitor kobuki's button events
		rospy.Subscriber("/mobile_base/events/button",ButtonEvent,self.ButtonEventCallback)

		#rospy.spin() tells the program to not exit until you press ctrl + c.  If this wasn't there... it'd subscribe and then immediatly exit (therefore stop "listening" to the thread).
		rospy.spin();


	
	def ButtonEventCallback(self,data):
	    if ( data.state == ButtonEvent.RELEASED ) :
		state = "released"
	    else:
		state = "pressed"  
	    if ( data.button == ButtonEvent.Button0 ) :
		button = "B0"
		GoToPose(x,y)
		#Go back to Dr. Barney Smith's office. Replace x and y arguments with first two pose coordinates seen on gmapping
	    elif ( data.button == ButtonEvent.Button1 ) :
		button = "B1"
		GoToPose(x1,y1)
		#Go back to charging station. Replace x and y arguments with first two pose coordinates seen on gmapping
	    else:
		button = "B2"
		print("Never gonna give you up \nNever gonna let you down \nNever gonna run around and desert you \nNever gonna make you cry \nNever gonna say goodbye \nNever gonna tell a lie and hurt you")
		#Resume navigation in the event of an interrupt event, ie. closed door, obstacle, etc.
		#Or play music/dance/rickroll
	    rospy.loginfo("Button %s was %s."%(button, state))
		

if __name__ == '__main__':
	try:
		kobuki_button()
	except rospy.ROSInterruptException:
		rospy.loginfo("exception")
