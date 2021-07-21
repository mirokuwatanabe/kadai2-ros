#!/usr/bin/env python3

#Copyright (c) 2022. ryuichiueda, mirokuwatanabe.
#License BSD.

import rospy
from std_msgs.msg import Float32

rospy.init_node('mode_selector')
pub = rospy.Publisher('mode', Float32, queue_size = 1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n = input("どれを計算しますか？\n1)溶媒の質量\n2)溶液の濃度\n3)溶質の質量\n")
    pub.publish(int(n))
    rate.sleep()
