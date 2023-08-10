#!/usr/bin/env python2
# Use iiwa/command/JointVelocity to control the robot's joints

import math
import rospy
import time
from iiwa_msgs.msg import JointVelocity, JointPosition

class VelocityController():
    KP=2
    MIN_ERROR=-6
    MAX_ERROR=6
    MAX_ANG_VEL=2
    PUBLISH_RATE=10
    
    def __init__(self):
        
        rospy.init_node('VelocityController', anonymous=0)
        self.time_now=rospy.Time.now()
        #Initialise the node VelocityController
        
        self.command_velocity=JointVelocity()
        self.current_position=JointPosition()
        self.goal_position=JointPosition()

        #Start the Publishing action
        self.pub=rospy.Publisher('/iiwa/command/JointVelocity', JointVelocity, queue_size=10)
        self.rate=rospy.Rate(self.PUBLISH_RATE)

        self.sub=rospy.Subscriber('/iiwa/command/JointVelocity', JointVelocity, self.command_velocity_callback)

    def command_velocity_callback(self, msg):
        self.command_velocity=msg
        return self.command_velocity

    def goal_position_callback(self, msg):
        self.goal_position=msg
        return self.goal_position
    
    def compute_error(self):
        if self.goal_position.position.a4 is not None and self.current_position.position.a4 is not None:
            self.raw_error=self.goal_position - self.current_position
            self.norm_error= 2 * (self.raw_error - self.MIN_ERROR) / (self.MAX_ERROR - self.MIN_ERROR) - 1
            self.command_velocity.velocity.a4=self.norm_error * self.KP
            print(self.norm_error, self.command_velocity.velocity.a4)

    def run(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.command_velocity)
            self.rate.sleep()

if __name__=='__main__':
    try:
        velocity_controller_object=VelocityController()
        velocity_controller_object.run()
    except rospy.ROSInterruptException():
        pass