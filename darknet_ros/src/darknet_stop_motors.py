#!/usr/bin/env python

import rospy,sys,roslib
from geometry_msgs.msg import Twist,Vector3
from master_node.srv import *
from std_msgs.msg import Int8


twistmessage = Twist()
twistmessage.linear.x = 0
twistmessage.angular.z = 0

requested_service = False

stop_service = rospy.ServiceProxy('stop',StopService)




def mainFunction():
    rospy.init_node('darknet_stop_motors', anonymous=True) # init a darknet_stop_motors node

    #Sottosrizione al topic object_detector
    rospy.Subscriber("/darknet_ros/object_detector",Int8,callback)

    rospy.loginfo("Stop Service Ready with DarknetROS")

    #REALEASE SULLO SHUTDOWN
    rospy.on_shutdown(print("Stop Service DarknetROS shutted down"))
    rospy.spin()



def callback(data):
	duck_found = data.data

	if((not requested_service) and duck_found != 0):
		stop_service(twistmessage)
		requested_service = True
	else:
		requested_service = False






if __name__ == "__main__":
	try:
		mainFunction()
	except rospy.ROSInterruptException:
		pass