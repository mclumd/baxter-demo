"""
Simple keyboard-controlled movement

When ran using the instructions found in the README file, this allows the user
to drive the mobility base using basic keyboard controls. When the user enters
one of the 6 recognized movement commands, the mobility base will move in that 
manner until told to stop or the reverse of that direction is entered. For 
example, if the user enters 'q', 'w', then 'e', each one second apart, the
mobility base will start by strafing left for one second, then moving forward 
while strafing left for a second, then moving forward while strafing right for
a second. 
"""
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
        self.cmd_pub_ = rospy.Publisher('/mobility_base/cmd_vel', Twist, queue_size=1)
        self.dist_thresh_ = 0.5
        self.speed = 0.05
        self.vel_ = Twist()
        self.vel_.linear.y = 0.0
        self.vel_.linear.z = 0.0

    def run_cmd(self, cmd):
        while (not rospy.is_shutdown()) and cmd_in_proc:
	    vel_to_command = 0
            try:
                rospy.sleep(0.01)
		if cmd == "w" or cmd == "s":
			if cmd == "w":
			    vel_to_command = self.speed
			elif cmd == "s":
			    vel_to_command = -self.speed
			self.vel_.linear.x = vel_to_command
		elif cmd == "a" or cmd == "d":		
			if cmd == "a":
			    vel_to_command = self.speed
			elif cmd == "d":
			    vel_to_command = -self.speed
			self.vel_.angular.z = vel_to_command * 2
                elif cmd == "q" or cmd == "e":
			if cmd == "q":
			    vel_to_command = self.speed
			elif cmd == "e":
			    vel_to_command = -self.speed
			self.vel_.linear.y = vel_to_command
		else:
			self.vel_.angular.z = 0
			self.vel_.linear.x = 0
                        self.vel_.linear.y = 0
                self.cmd_pub_.publish(self.vel_)
            except KeyboardInterrupt:
                print("Exiting")


def main(args):
    global cmd_in_proc
    mbn = MbNavigate()
    rospy.init_node('MbNavigate', anonymous=True)
    print("Press a recognized command, and then 'enter' to run the command. Recognized commands are as follows: 
[w]: forwards\n
[s]: backwards\n
[a]: turn left\n
[d]: turn right\n
[q]: strafe left\n
[e]: strafe right\n
[x]: halt\n
[xx]: halt and exit")
    while (not rospy.is_shutdown()):
        cmd = raw_input("Enter Command ['w', 's', 'a', 'd', 'q', 'e', or 'x']: \n")
	cmd_in_proc = False
	rospy.sleep(0.02)
        if cmd == "exit" or cmd == "xx":
            return
	cmd_in_proc = True
	t_cmd = Thread(target=mbn.run_cmd, args=(cmd,))
	t_cmd.start()
    
if __name__ == '__main__':
    main(sys.argv)

    
