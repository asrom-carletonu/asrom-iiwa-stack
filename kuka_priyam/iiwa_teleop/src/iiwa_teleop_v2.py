#!/usr/bin/env python2

from geometry_msgs.msg import PoseStamped
import time
import math
import rospy
import keyboard

if __name__=='__main__':
    try:
        rospy.init_node()
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    print('You Pressed A Key!')
                break  # finishing the loop
            except:
                break  # if user pressed a key other than the given key the loop will break
    except rospy.ROSInterruptException:
        pass