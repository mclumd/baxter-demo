import sys
import os
import numpy as np
import rospy
import socket
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from threading import Thread

cmd_in_proc = False

class MbNavigate:
    def __init__(self):
        '''Init ROS node, laser subs, and command pub'''
        self.cmd_pub_ = rospy.Publisher('/mobility_base/cmd_vel', Twist, queue_size=1)
        self.speed = 0.1  # default speed for movement
        self.vel_ = Twist()
        self.vel_.linear.y = 0.0
        self.vel_.linear.z = 0.0
        # Currently not using laser stuff, but left for possible future use (requires refactoring)
        #self.cmd_forward_ = False
        #self.cmd_backward_ = False
        #self.dist_thresh_ = 0.5
        #self.laser_front_sub_ = rospy.Subscriber("/laser_front_hokuyo/scan", LaserScan, self.laser_front_cb,  queue_size = 1)
        #self.laser_back_sub_ = rospy.Subscriber("/laser_rear_hokuyo/scan", LaserScan, self.laser_back_cb,  queue_size = 1)


    # Currently not using laser stuff, but left for possible future use (requires refactoring)
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
                elif cmd == "turn left" or cmd == "turn right":
                    if cmd == "turn left":
                        vel_to_command = self.speed
                    elif cmd == "turn right":
                        vel_to_command = -self.speed
                    self.vel_.angular.z = vel_to_command * 2
                else:
                    self.vel_.angular.z = 0
                    self.vel_.linear.x = 0

                # Publish command for execution
                self.cmd_pub_.publish(self.vel_)
            except KeyboardInterrupt:
                print("Exiting")

def getConnection():
    HOST = os.environ.get('ROS_HOSTNAME', 'NUC.local') # Should be one of 192.168.1.29 or 192.168.1.31
    PORT = 44545        # Port to listen on
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print('Listening on port {}'.format(PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection made with ', addr)
    return conn

def closeConnection(conn):
    print('CLOSING CONNECTION TO CLIENT...')
    conn.close()
    print('NOTE: May need to wait for TIME_WAIT to expire before running again')

def main(args):
    global cmd_in_proc
    mbn = MbNavigate()
    rospy.init_node('MbNavigate', anonymous=True)
    conn = None
    try:
        conn = getConnection()
        while (not rospy.is_shutdown()):
            cmd = conn.recv(1024).strip()
            print('RECVD: "{}"'.format(cmd))
            cmd_in_proc = False
            rospy.sleep(0.02)
            if cmd == "exit":
                break
            cmd_in_proc = True
            t_cmd = Thread(target=mbn.run_cmd, args=(cmd,))
            t_cmd.start()
    finally:
        if conn:
            closeConnection(conn)


if __name__ == '__main__':
    main(sys.argv)
