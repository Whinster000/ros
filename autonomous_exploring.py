#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
	print('=========================================')
	print('s1 [0]')
	print msg.ranges[0]

	print('s2 [45]')
	print msg.ranges[45]

	print('s3 [315]')
	print msg.ranges[315]

	#If obstacle is at least 0.5m in front of the TB3 in either 3 directions, the TB3 will move forward, else the TB3 will move 90 degrees per loop until there is clearance
	if msg.ranges[0] >= 0.5 and msg.ranges[45] >= 0.5 and msg.ranges[315] >= 0.5:
		move.linear.x = 0.3
		move.angular.z = 0.0
	elif msg.ranges[45] < 0.5:
		move.linear.x = 0.0
		move.angular.z = -1	#60 degrees to right
	elif msg.ranges[315] < 0.5:
		move.linear.x = 0.0
		move.angular.z = 1	#60 degrees to left
	else:
		move.linear.x = 0.0
		move.angular.z = 1.57	#90 degrees to left

	pub.publish(move)

rospy.init_node('exploring')			# Initiate a Node called 'exploring'
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()
