#!/usr/bin/env python

import rospy,sys,roslib
from master_node.srv import *
from std_msgs.msg import Int8


stop_service = rospy.ServiceProxy('stop',StopService)




def mainFunction():
    rospy.init_node('darknet_stop_motors', anonymous=True) # init a darknet_stop_motors node

    #Sottosrizione al topic object_detector
    rospy.Subscriber("/darknet_ros/found_object",Int8,callback)

    rospy.loginfo("Stop Service Ready with DarknetROS")

    #REALEASE SULLO SHUTDOWN
    #rospy.on_shutdown(print("Stop Service DarknetROS shutted down"))
    rospy.spin()



def callback(data):
	ducks_founded = data.data
	print(ducks_founded)


	if (ducks_founded > 0):
		print("Founded")
		stop_service(int(ducks_founded))






if __name__ == "__main__":
	try:
		mainFunction()
	except rospy.ROSInterruptException:
		pass
