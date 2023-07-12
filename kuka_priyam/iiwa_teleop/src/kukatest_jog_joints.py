#!/usr/bin/env python3

import math
import time
import rospy
from iiwa_msgs.msg import JointPosition

def JointPositionPublisher():
    jp0=JointPosition()
    
    jp1_1=JointPosition()
    jp1_2=JointPosition()
    
    jp2_1=JointPosition()
    jp2_2=JointPosition()
    
    jp3_1=JointPosition()
    jp3_2=JointPosition()
    
    jp4_1=JointPosition()
    jp4_2=JointPosition()
    
    jp5_1=JointPosition()
    jp5_2=JointPosition()
    
    jp6_1=JointPosition()
    jp6_2=JointPosition()
    
    jp7_1=JointPosition()
    jp7_2=JointPosition()

    jp7_1.position.a7=math.radians(-90)
    jp7_2.position.a7=math.radians(90)

    jp6_1.position.a6=math.radians(-90)
    jp6_2.position.a6=math.radians(90)

    jp5_1.position.a5=math.radians(-90)
    jp5_2.position.a5=math.radians(90)

    jp4_1.position.a4=math.radians(-90)
    jp4_2.position.a4=math.radians(90)

    jp3_1.position.a3=math.radians(-90)
    jp3_2.position.a3=math.radians(90)

    jp2_1.position.a2=math.radians(-90)
    jp2_2.position.a2=math.radians(90)

    jp1_1.position.a1=math.radians(-90)
    jp1_2.position.a1=math.radians(90)

    jpPublisher=rospy.Publisher('/iiwa/command/JointPosition', JointPosition, queue_size=10)
    rospy.init_node('joint_position_control', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing Position 7 min:")
        jpPublisher.publish(jp7_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 7 max:")
        jpPublisher.publish(jp7_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        rospy.loginfo("Publishing Position 6 min:")
        jpPublisher.publish(jp6_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 6 max:")
        jpPublisher.publish(jp6_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        rospy.loginfo("Publishing Position 5 min:")
        jpPublisher.publish(jp5_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 5 max:")
        jpPublisher.publish(jp5_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        rospy.loginfo("Publishing Position 4 min:")
        jpPublisher.publish(jp4_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 4 max:")
        jpPublisher.publish(jp4_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        rospy.loginfo("Publishing Position 3 min:")
        jpPublisher.publish(jp3_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 3 max:")
        jpPublisher.publish(jp3_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        rospy.loginfo("Publishing Position 2 min:")
        jpPublisher.publish(jp2_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 2 max:")
        jpPublisher.publish(jp2_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        rospy.loginfo("Publishing Position 1 min:")
        jpPublisher.publish(jp1_1)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        rospy.loginfo("Publishing Position 1 max:")
        jpPublisher.publish(jp1_2)
        time.sleep(4)
        rospy.loginfo("Publishing Position 0:")
        jpPublisher.publish(jp0)
        time.sleep(4)
        
        
if __name__=='__main__':
    try:
        JointPositionPublisher()
    except rospy.ROSInterruptException:
        pass