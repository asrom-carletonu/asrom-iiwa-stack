#!/usr/bin/env python2
# Use iiwa/command/JointVelocity to control the robot's joints

import math
import rospy
import time
from iiwa_msgs.msg import JointVelocity

class VeloCont():
    MAX_ANG_VEL=2
    PUBLISH_RATE=10
    def initialize(self):
        
        rospy.init_node('VelocityController', anonymous=0)
        self.timenow=rospy.Time.now()
        #Initialise the node VelocityController
        
        #Start the Publishing action
        self.pub=rospy.Publisher('/iiwa/command/JointVelocity', JointVelocity, queue_size=10)
        self.rate=rospy.Rate(self.PUBLISH_RATE)

        self.velo=JointVelocity()
        self.velo.velocity.a4=self.MAX_ANG_VEL*math.sin(0.5*(self.count))
        self.count+=0.1

        print(self.velo.velocity.a4)

    def Vpublish(self):
        self.initialize()
        self.pub.publish(self.velo)
        self.rate.sleep()

if __name__=='__main__':
    try:
        VC=VeloCont()
        VC.count=0
        while not rospy.is_shutdown():
            VC.Vpublish()
    except rospy.ROSInterruptException():
        pass