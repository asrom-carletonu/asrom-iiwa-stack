#!/usr/bin/env python

import rospy
from iiwa_msgs.msg import JointVelocity
from iiwa_msgs.msg import JointPosition

class JPVController():
    PUB_FREQ=10.0 #Hz
    # print(PUB_FREQ)
    MAX_VEL=0.2
    FAC=0.0
    FAC=1/PUB_FREQ
    # print(FAC)
    def __init__(self):
        # print(self.FAC)
        self.recievedJP=JointPosition()
        self.commandJPV=JointVelocity()
        # self.commandJPV.position.a4=0.5
        self.sub=rospy.Subscriber('/iiwa/state/JointPosition', JointPosition, self.updateCurrJP)
        rospy.init_node('incremental_JPV_controller', anonymous=False)
        self.pub=rospy.Publisher('/iiwa/command/JointVelocity', JointVelocity, queue_size=10)
        self.pub_rate=rospy.Rate(self.PUB_FREQ)
        # print('publishing to /iiwa/command/JointPositionVelocity')

    def updateCurrJP(self,msg):
        self.recievedJP=msg
        # if self.recievedJP.position.a4 >= 1.5:
        #     self.commandJPV.position.a4=1.5
        #     self.commandJPV.velocity.a4=0
        #     rospy.signal_shutdown()
        # print(self.recievedJP.position.a4)
        
        # print("updated commandJPV")


    def JPVPubFunc(self):
        while not rospy.is_shutdown():
            # self.commandJPV.position.a4=self.commandJPV.position.a4 + self.MAX_VEL*self.FAC
            self.NOW=rospy.get_time()
            print(self.MAX_VEL*self.FAC, self.NOW)
            self.commandJPV.velocity.a4=self.MAX_VEL
            self.pub.publish(self.commandJPV)
            # print("#######################################################################################")
            # print(self.FAC)
            self.pub_rate.sleep()

if __name__ == '__main__':
    JPVObj=JPVController()
    while not rospy.is_shutdown():
        try:
            JPVObj.JPVPubFunc()
        except rospy.ROSInterruptException():
            pass