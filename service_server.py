#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import *

def sum_2_ints(req):
    return AddTwoIntsResponse(req.a+req.b)
        
def service():
    rospy.init_node('add_two_ints_server')
    rospy.Service('add_two_ints', AddTwoInts, sum_2_ints)
    rospy.spin()

if __name__ == '__main__':
    service()
