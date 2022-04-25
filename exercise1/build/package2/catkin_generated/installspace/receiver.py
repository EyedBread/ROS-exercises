#!/usr/bin/env python2


import rospy
from std_msgs.msg import UInt32, Float32

rospy.init_node('nodeB', anonymous=True)
pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
rate = rospy.Rate(20)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    res = div(float(data.data),0.15)
    pub.publish(res)

def div(input,q):
    return (input/q)

def receiver():

    rospy.Subscriber('angelic', UInt32, callback)

    rospy.spin()

if __name__ == '__main__':
    receiver()
