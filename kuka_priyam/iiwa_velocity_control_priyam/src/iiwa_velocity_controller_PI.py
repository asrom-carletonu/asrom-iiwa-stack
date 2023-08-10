#!/usr/bin/env python2
# Use iiwa/command/JointVelocity to control the robot's joints

import math
import rospy
import time
from iiwa_msgs.msg import JointVelocity, JointPosition

class VelocityController():
    KP=0.5
    KI=0.000001
    I_SAT=1.0
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
        self.integral=0

        #Start the Publishing action
        self.pub=rospy.Publisher('/iiwa/dummy/command/JointVelocity', JointVelocity, queue_size=10)
        # self.pub=rospy.Publisher('/iiwa/command/JointVelocity', JointVelocity, queue_size=10)
        # self.r=rospy.Rate(self.PUBLISH_RATE)
        self.dur=rospy.Duration(0,100000000)
        self.sub=rospy.Subscriber('/iiwa/state/JointPosition', JointPosition, self.current_position_callback)
        self.sub=rospy.Subscriber('/iiwa/goal/JointPosition', JointPosition, self.goal_position_callback)

        print("init successfully")

    def current_position_callback(self, msg):
        self.current_position=msg
        # print(self.current_position)
        # return self.current_position

    def goal_position_callback(self, msg):
        self.goal_position=msg
        # return self.goal_position
    
    def compute_error(self):
        if self.goal_position.position.a4 is not None and self.current_position.position.a4 is not None:
            self.raw_error=self.goal_position.position.a4 - self.current_position.position.a4 
            self.norm_error= 2 * (self.raw_error - self.MIN_ERROR) / (self.MAX_ERROR - self.MIN_ERROR) - 1
            self.integral += self.norm_error
            self.command_velocity.velocity.a4 = self.KP * self.norm_error + self.KI * self.integral 
            print('%f' %self.integral, '%f' %self.norm_error, '%f' %self.command_velocity.velocity.a4)

            self.pub.publish(self.command_velocity)

    def run(self):
            print("enter loop")
            self.compute_error()            
            rospy.sleep(self.dur)

if __name__=='__main__':
    try:
        velocity_controller_object=VelocityController()
        while not rospy.is_shutdown():
            velocity_controller_object.run()
    except rospy.ROSInterruptException():
        pass