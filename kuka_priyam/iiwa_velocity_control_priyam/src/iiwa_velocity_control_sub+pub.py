#!/usr/bin/env python

# Use iiwa/command/JointVelocity to control the robot's joints

import math
import rospy
import time
from iiwa_msgs.msg import JointVelocity
from iiwa_msgs.msg import JointPosition

class VelocityController():
    FREQ=1
    # rospy.init_node('VelocityControllerNode', anonymous=False)
    
    def stateReader(self):
        rospy.init_node('StateReaderNode', anonymous=False)
        rospy.Subscriber('/iiwa/state/JointPosition', JointPosition, self.publishVelocities)

    # def updateVelocity(self):
        # rospy.loginfo("Velocity updated")
        # self.now=rospy.get_rostime()
        # self.velocity=JointVelocity()
        # self.timevar=float(self.now.secs+self.now.nsecs*0.000001)
        # rospy.loginfo("%f , %f", self.now.secs, self.now.nsecs)
        # self.velocity.velocity.a6=0.1#math.sin(self.timevar/1000)

    def publishVelocities(self,msg):
        self.currentJV=JointPosition()
        self.currentJV=msg
        # self.rate=rospy.Rate(self.FREQ)
        rospy.loginfo('%f  |  %f  |  %f |  %f  |  %f  |  %f  |  %f', self.currentJV.position.a1,self.currentJV.position.a2,self.currentJV.position.a3,self.currentJV.position.a4,self.currentJV.position.a5,self.currentJV.position.a6,self.currentJV.position.a7)
        
        # self.updateVelocity()   
        # rospy.loginfo("Velocity published, %f", self.velocity.velocity.a6)
        # VelocityPublisher=rospy.Publisher('/iiwa/command/JointVelocity', JointVelocity, queue_size=10)
        # VelocityPublisher.publish(self.velocity)
        # rospy.sleep(0.1)

if __name__=='__main__':
    velocityController=VelocityController()
    while not rospy.is_shutdown():
        try:
            velocityController.stateReader()
        except rospy.ROSInterruptException():
            pass