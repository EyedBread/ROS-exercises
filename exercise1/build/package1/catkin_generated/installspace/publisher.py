#!/usr/bin/env python2


import rospy
from std_msgs.msg import UInt32

def publisher():
    pub = rospy.Publisher('angelic', UInt32, queue_size=10)
    rospy.init_node('nodeA', anonymous=True)
    rate = rospy.Rate(20) 
    k = 0
    while not rospy.is_shutdown():
        k = k + 4
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
