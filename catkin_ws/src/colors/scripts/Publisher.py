#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import Int32
from colors.msg import Num


class Publisher:

    def __init__(self, from_topic):
        self.rate = rospy.Rate(1) # 10hz
        self.pub = rospy.Publisher(from_topic, Num, queue_size=10)
        self.create_message()

    def talk(self, to_publish):
        rospy.loginfo('I send %s',to_publish)
        self.pub.publish(to_publish)

    def create_message(self):
        while not rospy.is_shutdown():
            message = Num()
            message.R = self.rand_colorcode()
            message.G = self.rand_colorcode()
            message.B = self.rand_colorcode()
            self.talk(message)
            self.rate.sleep()

    @staticmethod
    def rand_colorcode():
        return random.randrange(0,255)


if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    try:
        Publisher("randomNumberGenerator")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    