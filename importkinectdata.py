#first command is to start up the nodelets with the launch file
#roslaunch openni_launch openni.launch
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image
class image_to_cv2:
	def __init__(self):
    # initialize a node called hw2
    	rospy.init_node("imgload")
    # create a window to display results in
    	cv2.namedWindow("image_view", cv2.WINDOW_NORMAL)
    # subscribe to the 'image' topic
    #still need to confirm if its actually the topic name for Kinect input
    	self.image_sub = rospy.Subscriber("image", Image, self.callback)
    def callback(self, data):
    	bridge=CvBridge()
    	try:
    		cv_image=bridge.img_to_cv(data, "bgr8")
    	except CvBridgeError, e:
    		#print won't work, need to use rospy.log_ format
    		rospy.loginfo("Media failed to convert to OpenCV format")
    	#we can edit the image below and do stuff to it
    	#cv_image=...
    #displays image in previously created window
    cv2.imshow("image_view",cv_image)
    #delays for 3 miliseconds
    cv2.WaitKey(3)
'''__main__ is default value assigned to scripts executed directly,
loops the script'''
if __name__ == '__main__':
    image_to_cv2()
    try:  
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"
    cv2.DestroyAllWindows()
	
