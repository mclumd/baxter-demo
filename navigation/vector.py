"""
Moves the mobility base according to entered vectors

When run using the instructions in the README document, this script allows the
the user to enter a time-vector for the mobility base to move in. While moving, 
the base will not turn; it will only move forward/backward and laterally (using
the strafing capabilities of the mecanum wheels). 
"""
import sys
import numpy as np
import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from threading import Thread

cmd_in_proc = False

class MbNavigate:
    def __init__(self):
        '''Init ROS node, laser subs, and command pub'''
        self.cmd_pub_ = rospy.Publisher('/mobility_base/cmd_vel', Twist, queue_size=1)
        self.dist_thresh_ = 0.5
        self.speed = 0.1
        #self.speed = 0.05
        self.vel_ = Twist()
        self.vel_.linear.y = 0.0
        self.vel_.linear.z = 0.0

    def move_vector(self, time, angle):
        counter = 0
        angle = 0 - angle
        self.vel_.linear.x = self.speed * math.cos(math.radians(angle))
        self.vel_.linear.y = self.speed * math.sin(math.radians(angle))
        while (counter < time):
            self.cmd_pub_.publish(self.vel_)
            rospy.sleep(0.01)
            counter += 0.01
                
def main(args):
    global cmd_in_proc
    mbn = MbNavigate()
    rospy.init_node('MbNavigate', anonymous=True)
    while (not rospy.is_shutdown()):
        time = input("Enter a duration in seconds:\n")
        angle = input("Enter an angle in degrees (0 = forward):\n") 
        mbn.move_vector(time, angle)
    
if __name__ == '__main__':
    main(sys.argv)

    
