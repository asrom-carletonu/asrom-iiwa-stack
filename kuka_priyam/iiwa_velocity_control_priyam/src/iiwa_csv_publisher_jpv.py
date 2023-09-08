#!/usr/bin/env python

import rospy
import os
import csv
from iiwa_msgs.msg import JointPositionVelocity

class JPVController():
    PUB_FREQ=1000.0 #Hz
    # print(PUB_FREQ)
    MAX_VEL=0.2
    FAC=0.0
    FAC=1/PUB_FREQ

    def __init__(self):

        self.JPA1 = []
        self.JPA2 = []
        self.JPA3 = []
        self.JPA4 = []
        self.JPA5 = []
        self.JPA6 = []
        self.JPA7 = []
        
        self.JVA1 = []
        self.JVA2 = []
        self.JVA3 = []
        self.JVA4 = []
        self.JVA5 = []
        self.JVA6 = []
        self.JVA7 = []
        
        with open("/home/asromws/Downloads/traj.csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
            for column in reader: # each row is a list
                self.JPA1.append(column[0])
                self.JPA2.append(column[1])
                self.JPA3.append(column[2])
                self.JPA4.append(column[3])
                self.JPA5.append(column[4])
                self.JPA6.append(column[5])
                self.JPA7.append(column[6])

                self.JVA1.append(column[7])
                self.JVA2.append(column[8])
                self.JVA3.append(column[9])
                self.JVA4.append(column[10])
                self.JVA5.append(column[11])
                self.JVA6.append(column[12])
                self.JVA7.append(column[13])

        # print(self.JPA1)
        # print(self.JVA1)
        self.count=0
        self.commandJPV = JointPositionVelocity()

        self.recievedJP=JointPositionVelocity()
        rospy.init_node('incremental_JPV_controller', anonymous=False)
        self.pub=rospy.Publisher('/iiwa/command/JointPositionVelocity', JointPositionVelocity, queue_size=10)
        self.pub_rate=rospy.Rate(self.PUB_FREQ)
        

    def JPVPubFunc(self):
        while not rospy.is_shutdown():

            self.commandJPV.position.a1 = self.JPA1[self.count]
            self.commandJPV.position.a2 = self.JPA2[self.count]
            self.commandJPV.position.a3 = self.JPA3[self.count]
            self.commandJPV.position.a4 = self.JPA4[self.count]
            self.commandJPV.position.a5 = self.JPA5[self.count]
            self.commandJPV.position.a6 = self.JPA6[self.count]
            self.commandJPV.position.a7 = self.JPA7[self.count]

            self.commandJPV.velocity.a1 = self.JVA1[self.count]
            self.commandJPV.velocity.a2 = self.JVA2[self.count]
            self.commandJPV.velocity.a3 = self.JVA3[self.count]
            self.commandJPV.velocity.a4 = self.JVA4[self.count]
            self.commandJPV.velocity.a5 = self.JVA5[self.count]
            self.commandJPV.velocity.a6 = self.JVA6[self.count]
            self.commandJPV.velocity.a7 = self.JVA7[self.count]

            print(self.commandJPV)
            self.pub.publish(self.commandJPV)
            self.count+=1
            self.pub_rate.sleep()

if __name__ == '__main__':
    JPVObj=JPVController()
    while not rospy.is_shutdown():
        try:
            JPVObj.JPVPubFunc()
        except rospy.ROSInterruptException():
            pass