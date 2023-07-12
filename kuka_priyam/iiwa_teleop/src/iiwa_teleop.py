#!/usr/bin/env python2

from geometry_msgs.msg import PoseStamped
import time
import math
import rospy


def PositionPublisher():

    CartPos1 = PoseStamped()
    CartPos1.pose.position.x=0.3
    CartPos1.pose.position.y=0.3
    CartPos1.pose.position.z=1.0
    CartPos1.pose.orientation.x=0.0
    CartPos1.pose.orientation.y=0.0
    CartPos1.pose.orientation.z=0.3826834
    CartPos1.pose.orientation.w=0.9238795

    CartPos2 = PoseStamped()
    CartPos2.pose.position.x=-0.3
    CartPos2.pose.position.y=0.3
    CartPos2.pose.position.z=1.0
    CartPos2.pose.orientation.x=0.0
    CartPos2.pose.orientation.y=0.0
    CartPos2.pose.orientation.z=0.9238795
    CartPos2.pose.orientation.w=0.3826834

    CartPos3 = PoseStamped()
    CartPos3.pose.position.x=-0.3
    CartPos3.pose.position.y=-0.3
    CartPos3.pose.position.z=1.0
    CartPos3.pose.orientation.x=0.0
    CartPos3.pose.orientation.y=0.0
    CartPos3.pose.orientation.z=0.9238795
    CartPos3.pose.orientation.w=-0.3826834

    CartPos4 = PoseStamped()
    CartPos4.pose.position.x=0.3
    CartPos4.pose.position.y=-0.3
    CartPos4.pose.position.z=1.0
    CartPos4.pose.orientation.x=0.0
    CartPos4.pose.orientation.y=0.0
    CartPos4.pose.orientation.z=0.3826834
    CartPos4.pose.orientation.w=-0.9238795

    cartPublisher=rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size=10)
    rospy.init_node('cartesian_position_control', anonymous=False)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # rospy.loginfo("#########################################################")
        cartPublisher.publish(CartPos1)
        time.sleep(8)
        cartPublisher.publish(CartPos2)
        time.sleep(8)
        cartPublisher.publish(CartPos3)
        time.sleep(8)
        cartPublisher.publish(CartPos4)
        time.sleep(8)
        

if __name__=='__main__':
    try:
        PositionPublisher()
    except rospy.ROSInterruptException:
        rospy.loginfo("QUIT")
        pass