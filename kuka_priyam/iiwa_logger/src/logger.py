#!/usr/bin/env python

import rospy
from iiwa_msgs.msg import JointPosition, JointVelocity, JointTorque
import csv
from datetime import datetime
import os

class DataLogger:
    def __init__(self):
        self.JPcsv_file_path = self.generate_JP_csv_file_path()
        self.JVcsv_file_path = self.generate_JV_csv_file_path()
        self.JTcsv_file_path = self.generate_JT_csv_file_path()

        rospy.init_node('data_logger', anonymous=True)
        
        self.joint_positions = JointPosition()
        self.joint_velocities = JointVelocity()
        self.joint_torques = JointTorque()
        
        self.JPcsv_file = open(self.JPcsv_file_path, 'a')  # Open the CSV file
        self.JVcsv_file = open(self.JVcsv_file_path, 'a')  # Open the CSV file
        self.JTcsv_file = open(self.JTcsv_file_path, 'a')  # Open the CSV file
        
        self.csv_data_titles(self.JPcsv_file)  # Pass the csv_file object to csv_data_titles
        self.csv_data_titles(self.JVcsv_file)  # Pass the csv_file object to csv_data_titles
        self.csv_data_titles(self.JTcsv_file)  # Pass the csv_file object to csv_data_titles
        
        rospy.Subscriber('/iiwa/state/JointPosition', JointPosition, self.JPcallback)
        rospy.Subscriber('/iiwa/state/JointVelocity', JointVelocity, self.JVcallback)
        rospy.Subscriber('/iiwa/state/JointTorque', JointTorque, self.JTcallback)

    def csv_data_titles(self, csv_file):
        writer = csv.writer(csv_file)
        writer.writerow(["Time", "Joint 1", "Joint 2", "Joint 3", "Joint 4", "Joint 5", "Joint 6", "Joint 7"])

    def generate_JP_csv_file_path(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        pathh = os.path.join(desktop_path, 'data_{}_JP.csv'.format(current_time))
        return pathh

    def generate_JV_csv_file_path(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        pathh = os.path.join(desktop_path, 'data_{}_JV.csv'.format(current_time))
        return pathh

    def generate_JT_csv_file_path(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        pathh = os.path.join(desktop_path, 'data_{}_JT.csv'.format(current_time))
        return pathh

    def JPcallback(self, msg):
        timestamp = rospy.get_rostime()
        timestamp_str = datetime.fromtimestamp(timestamp.to_sec()).strftime('%Y-%m-%d %H:%M:%S.%f')
        joint_positions = msg
        self.j1P = joint_positions.position.a1
        self.j2P = joint_positions.position.a2
        self.j3P = joint_positions.position.a3
        self.j4P = joint_positions.position.a4
        self.j5P = joint_positions.position.a5
        self.j6P = joint_positions.position.a6
        self.j7P = joint_positions.position.a7
        print(joint_positions)

        with open(self.JPcsv_file_path, 'a') as self.JPcsv_file:
            writer = csv.writer(self.JPcsv_file)
            writer.writerow([timestamp_str] + [self.j1P] + [self.j2P] + [self.j3P] + [self.j4P] + [self.j5P] + [self.j6P] + [self.j7P])

    def JVcallback(self, msg):
        timestamp = rospy.get_rostime()
        timestamp_str = datetime.fromtimestamp(timestamp.to_sec()).strftime('%Y-%m-%d %H:%M:%S.%f')
        joint_velocities = msg
        self.j1V = joint_velocities.velocity.a1
        self.j2V = joint_velocities.velocity.a2
        self.j3V = joint_velocities.velocity.a3
        self.j4V = joint_velocities.velocity.a4
        self.j5V = joint_velocities.velocity.a5
        self.j6V = joint_velocities.velocity.a6
        self.j7V = joint_velocities.velocity.a7
        print(joint_velocities)

        with open(self.JVcsv_file_path, 'a') as self.JVcsv_file:
            writer = csv.writer(self.JVcsv_file)
            writer.writerow([timestamp_str] + [self.j1V] + [self.j2V] + [self.j3V] + [self.j4V] + [self.j5V] + [self.j6V] + [self.j7V])

    def JTcallback(self, msg):
        timestamp = rospy.get_rostime()
        timestamp_str = datetime.fromtimestamp(timestamp.to_sec()).strftime('%Y-%m-%d %H:%M:%S.%f')
        joint_torques = msg
        self.j1T = joint_torques.torque.a1
        self.j2T = joint_torques.torque.a2
        self.j3T = joint_torques.torque.a3
        self.j4T = joint_torques.torque.a4
        self.j5T = joint_torques.torque.a5
        self.j6T = joint_torques.torque.a6
        self.j7T = joint_torques.torque.a7
        print(joint_torques)

        with open(self.JTcsv_file_path, 'a') as self.JTcsv_file:
            writer = csv.writer(self.JTcsv_file)
            writer.writerow([timestamp_str] + [self.j1T] + [self.j2T] + [self.j3T] + [self.j4T] + [self.j5T] + [self.j6T] + [self.j7T])

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    logger = DataLogger()
    while not rospy.is_shutdown():
        try:
            logger.run()
        except rospy.ROSInterruptException:
            pass
# #!/usr/bin/env python

# import rospy
# from iiwa_msgs.msg import JointPosition, JointVelocity, JointTorque
# import csv
# from datetime import datetime
# import os

# class DataLogger:
#     def __init__(self):
#         self.csv_file_path = self.generate_csv_file_path()
#         rospy.init_node('data_logger', anonymous=True)
#         self.joint_positions=JointPosition()
#         self.joint_velocities=JointVelocity()
#         self.joint_torques=JointTorque()
#         rospy.Subscriber('/iiwa/state/JointPosition', JointPosition, self.JPcallback)
#         # rospy.Subscriber('/iiwa/state/JointVelocity', JointVelocity, self.JVcallback)
#         # rospy.Subscriber('/iiwa/state/JointTorque', JointTorque, self.JTcallback)

#     def generate_csv_file_path(self):
#         desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#         current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
#         pathh = os.path.join(desktop_path, 'data_{}.csv'.format(current_time))
#         # print(current_time)
#         # print(pathh)
#         return pathh

#     def JPcallback(self,msg):
#         timestamp = rospy.get_rostime()
#         timestamp_str = datetime.fromtimestamp(timestamp.to_sec()).strftime('%Y-%m-%d %H:%M:%S.%f')
#         joint_positions = msg
#         self.j1=joint_positions.position.a1
#         self.j2=joint_positions.position.a2
#         self.j3=joint_positions.position.a3
#         self.j4=joint_positions.position.a4
#         self.j5=joint_positions.position.a5
#         self.j6=joint_positions.position.a6
#         self.j7=joint_positions.position.a7        
#         print(joint_positions)

#         with open(self.csv_file_path, 'a') as csv_file:
#             writer = csv.writer(csv_file)
#             writer.writerow([timestamp_str] + [self.j1]+ [self.j2]+ [self.j3]+ [self.j4]+ [self.j5]+ [self.j6]+ [self.j7])
    

#     def run(self):
#         rospy.spin()

# if __name__ == '__main__':
#     logger = DataLogger()
#     while not rospy.is_shutdown():
#         try:
#             logger.run()
#         except rospy.ROSInterruptException():
#             pass
####################################################################################################
# 
