import sys
import numpy as np
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from threading import Thread

cmd_in_proc = False

class MbNavigate:
    def __init__(self):
        '''Init ROS node, laser subs, and command pub'''
        #self.laser_front_sub_ = rospy.Subscriber("/laser_front_hokuyo/scan", LaserScan, self.laser_front_cb,  queue_size = 1)
        #self.laser_back_sub_ = rospy.Subscriber("/laser_rear_hokuyo/scan", LaserScan, self.laser_back_cb,  queue_size = 1)
        self.cmd_pub_ = rospy.Publisher('/mobility_base/cmd_vel', Twist, queue_size=1)
        self.dist_thresh_ = 0.5
        self.speed = 0.1
        self.vel_ = Twist()
        self.vel_.linear.y = 0.0
        self.vel_.linear.z = 0.0
        self.cmd_forward_ = False
        self.cmd_backward_ = False

        
    '''def laser_front_cb(self, data):
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
    '''
    
    def run_cmd(self, cmd):
        while (not rospy.is_shutdown()) and cmd_in_proc:
	    vel_to_command = 0
            try:
                rospy.sleep(0.01)
		if cmd == "forward" or cmd == "backward":
			if cmd == "forward":
			    vel_to_command = self.speed
			elif cmd == "backward":
			    vel_to_command = -self.speed
			self.vel_.linear.x = vel_to_command
		elif cmd == "left" or cmd == "right":		
			if cmd == "left":
			    vel_to_command = self.speed
			elif cmd == "right":
			    vel_to_command = -self.speed
			self.vel_.angular.z = vel_to_command * 2
		else:
			self.vel_.angular.z = 0
			self.vel_.linear.x = 0
                self.cmd_pub_.publish(self.vel_)
            except KeyboardInterrupt:
                print("Exiting")
    
    def issue_cmd(self,cmd):
	stop = False
        if cmd == "forward":
            self.cmd_forward_ = True
	    self.cmd_backward_ = False
        elif cmd == "backward":
            self.cmd_backward_ = True
	    self.cmd_forward_ = False
	else:
	    self.cmd_forward_ = False
	    self.cmd_backward_ = False
	    stop = True
        self.run_cmd()

def main(args):
    global cmd_in_proc
    mbn = MbNavigate()
    rospy.init_node('MbNavigate', anonymous=True)
    while (not rospy.is_shutdown()):
        cmd = raw_input("Enter Command ['forward', 'backward', 'left', 'right' or 'exit']: \n")
	cmd_in_proc = False
	rospy.sleep(0.02)
        if cmd == "exit":
            return
	cmd_in_proc = True
	t_cmd = Thread(target=mbn.run_cmd, args=(cmd,))
	t_cmd.start()

    
if __name__ == '__main__':
    main(sys.argv)

    
