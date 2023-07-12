#!/usr/bin/env python2
# Use iiwa/command/JointVelocity to control the robot's joints

import math
import rospy
# import time
from iiwa_msgs.msg import JointPositionVelocity

class VeloCont():
    MAX_ANG_VEL=2
    PUBLISH_RATE=10
        
    def initialize(self):
        
        rospy.init_node('VelocityController', anonymous=0)
        # self.timenow=rospy.Time.now()    
        #Start the Publishing action
        self.pub=rospy.Publisher('/iiwa/command/JointPositionVelocity', JointPositionVelocity, queue_size=10)
        self.rate=rospy.Rate(self.PUBLISH_RATE)
        self.JPV=JointPositionVelocity()
        self.JPV.position.a4=self.count#self.MAX_ANG_VEL*math.sin(0.2*(self.count))
        self.JPV.velocity.a4=0.8

        if self.count >= 1.6:
            self.JPV.velocity.a4=0
            self.JPV.position.a4=1.6
            # rospy.signal_shutdown()
    
        self.count+=0.08
        print(self.JPV.position.a4)

    def Vpublish(self):
        self.initialize()
        self.pub.publish(self.JPV)
        self.rate.sleep()

if __name__=='__main__':
    try:
        VC=VeloCont()
        VC.count=-1.6
        while not rospy.is_shutdown():
            VC.Vpublish()
    except rospy.ROSInterruptException():
        pass