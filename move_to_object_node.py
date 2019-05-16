#!/usr/bin/python
import rospy
from find_object_2d.msg import DetectionInfo
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def callback(data):
    rospy.loginfo("Recieved {0}".format(data.data))
    twist = Twist()
    if data.data # If data present an object was detected, move forward
        twist.linear.x = .10; twist.linear.y = 0.0; twist.linear.z = 0.0;
        twist.angular. = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0;
    else #if not present, no object detected, spin
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0;
        twist.angular. = 0.0; twist.angular.y = 0.0; twist.angular.z = .5;

    pub.publish(twist)


def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("/objects", Float32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()