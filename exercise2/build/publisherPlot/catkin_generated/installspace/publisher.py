#!/usr/bin/env python2

import rospy
from std_msgs.msg import Float64

def publisher():
    pub = rospy.Publisher('plotting', Float64, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(5) 
    k = 0
    while not rospy.is_shutdown():
        k = k + 0.01
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()



if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass