import sys
import numpy as np
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MbNavigate:
    def __init__(self):
        '''Init ROS node, laser subs, and command pub'''
        self.laser_front_sub_ = rospy.Subscriber("/laser_front_hokuyo/scan", LaserScan, self.laser_front_cb,  queue_size = 1)
        self.laser_back_sub_ = rospy.Subscriber("/laser_rear_hokuyo/scan", LaserScan, self.laser_back_cb,  queue_size = 1)
        self.cmd_pub_ = rospy.Publisher('/mobility_base/cmd_vel', Twist, queue_size=1)
        self.dist_thresh_ = 0.5
        self.speed = 0.4
        self.vel_ = Twist()
        self.vel_.linear.y = 0.0
        self.vel_.linear.z = 0.0
        self.cmd_forward_ = False
        self.cmd_backward_ = False
        
    def laser_front_cb(self, data):
        if self.cmd_forward_ == True and self.cmd_backward_ == False:
            ranges = np.asarray(data.ranges)
            if np.min(ranges) > self.dist_thresh_:
                self.vel_.linear.x = self.speed
                self.cmd_pub_.publish(self.vel_)
            else:
                self.cmd_forward_ = False
            
    def laser_back_cb(self, data):
        if self.cmd_backward_ == True and self.cmd_forward_ == False:
            ranges = np.asarray(data.ranges)
            if np.min(ranges) > self.dist_thresh_:
                self.vel_.linear.x = -self.speed
                self.cmd_pub_.publish(self.vel_)
            else:
                self.cmd_backward_ = False
            return
    
    def run_cmd(self):
        while (not rospy.is_shutdown()) and (self.cmd_forward_ or self.cmd_backward_):
            try:
                rospy.sleep(0.01)
            except KeyboardInterrupt:
                print("Exiting")
    
    def issue_cmd(self,cmd):
        if cmd == "Forward":
            self.cmd_forward_ = True
        elif cmd == "Backward":
            self.cmd_backward_ = True
        self.run_cmd()

def main(args):
    mbn = MbNavigate()
    rospy.init_node('MbNavigate', anonymous=True)
    while (not rospy.is_shutdown()):
        cmd = raw_input("Enter Command ['Forward' or 'Backward' or 'exit']: \n")
        if cmd == "exit":
            return
        mbn.issue_cmd(cmd)
    
if __name__ == '__main__':
    main(sys.argv)

    