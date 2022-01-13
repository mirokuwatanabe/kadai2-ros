#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

x0 = 0
y0 = 0
z0 = 0
A0 = 0
x1 = float(x0)
y1 = float(y0)
z1 = float(z0)
A1 = float(A0)
n = 0

def cb(message):
    global A1
    n = message.data
    
    #mode 1
    if(int(n) == 1):
        x1 = input("溶液の濃度を入力してください(%): ")
        y1 = input("溶質の質量を入力してください(g): ")
        z1 = 100
        A1 = (float(z1) * float(y1) / float(x1)) - float(y1)
        print("別窓に表示します(g)")
        pub.publish(A1)
    
    #mode 2
    elif(int(n) == 2):
        x1 = input("溶質の質量を入力してください(g): ")
        y1 = input("溶媒の質量を入力してください(g): ")
        z1 = 100
        A1 = float(x1) / (float(x1) + float(y1)) * float(z1)
        print("別窓に表示します(%)")
        pub.publish(A1)
    
    #mode 3
    elif(int(n) == 3):
        x1 = input("溶液の濃度を入力してください(%): ")
        y1 = input("溶媒の質量を入力してください(g): ")
        z1 = 100
        A1 = (float(z1) * float(y1) /float(x1)) - float(y1)
        print("別窓に表示します(g)")
        pub.publish(A1)

    else:
        print("不正な数値です")

rospy.init_node('answer')
sub = rospy.Subscriber('mode', Float32, cb)
pub = rospy.Publisher('answer', Float32, queue_size =  1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
