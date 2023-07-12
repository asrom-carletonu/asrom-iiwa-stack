#!/usr/bin/env python2
# Use iiwa/command/JointVelocity to control the robot's joints

import math
import rospy
import time
from geometry_msgs.msg import PoseStamped
from iiwa_msgs.msg import JointPosition

class CartCont():
    MAX_ANG_VEL=2
    PUBLISH_RATE=10
        
    def initialize(self):
        rospy.init_node('CartesianController', anonymous=0)
        self.timenow=rospy.Time.now()    
        #Start the Publishing action
        self.pub=rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size=10)
        self.rate=rospy.Rate(self.PUBLISH_RATE)
        # self.pub=rospy.Publisher('/iiwa/command/JointPosition', JointPosition, queue_size=10)
        # self.rate=rospy.Rate(self.PUBLISH_RATE)
        if self.count == 0:
            # self.jp=JointPosition()
            self.cart=PoseStamped()
            self.cartStart()
            # self.goToStart()
        self.linearMovement()

    # def goToStart(self):
    #     rospy.loginfo('going to start postion')

    #     self.jp.position.a1=math.radians(12.45)
    #     self.jp.position.a2=math.radians(46.79)
    #     self.jp.position.a3=math.radians(-35.42)
    #     self.jp.position.a4=math.radians(77.99)
    #     self.jp.position.a5=math.radians(-70.74)
    #     self.jp.position.a6=math.radians(82.05)
    #     self.jp.position.a7=math.radians(-3.48)

    def cartStart(self):
        self.cart.pose.position.x=0.08247#2+self.count
        self.cart.pose.position.y=0.15714
        self.cart.pose.position.z=0.988#-self.count
        self.cart.pose.orientation.x=0.940861
        self.cart.pose.orientation.y=-0.1297888
        self.cart.pose.orientation.z=0.2732354
        self.cart.pose.orientation.w=0.1525707
        print(self.cart.pose.position.x)


    def linearMovement(self):
        # self.count+=0.00001
        # if bool:
        #     increment
        # elif bool:
        #     decrement
        if self.cart.pose.position.x >= -0.5:
            self.cart.pose.position.x-=self.count
        else:
            pass
            # rospy.signal_shutdown()
        print("linearmove")


    def Vpublish(self):
        self.initialize()
        # if self.count<=0.001:
        # self.pub.publish(self.jp)
        # else:

        self.pub.publish(self.cart)
        self.rate.sleep()

if __name__=='__main__':
    try:
        VC=CartCont()
        VC.count=0
        while not rospy.is_shutdown():
            VC.Vpublish()
            # if VC.count==1000:
            #     rospy.signal_shutdown()
    except rospy.ROSInterruptException():
        pass