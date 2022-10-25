#!/usr/bin/env python3
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String
from colors.msg import Num

class Forwarder:

    def __init__(self, from_topic, to_topic):
        self.pub = rospy.Publisher(from_topic, String, queue_size=10)
        self.subscriber = rospy.Subscriber(to_topic, Num, self.callback)

    def talk(self, to_publish):
        rospy.loginfo('I send %s',to_publish)
        self.pub.publish(to_publish)


    def callback(self, msg_data):
        average = self.calc_avg(msg_data.R, msg_data.G, msg_data.B)
        if average >= 180:
            category = "HIGH"
        elif average< 100:
            category = "LOW"
        else: category = "MEDIUM"
        
        self.talk(to_publish=category)

        rospy.loginfo(rospy.get_caller_id() + ' %s %i', category, average)


    @staticmethod
    def calc_avg(a,b,c):
        list = [a,b,c]
        return sum(list)/len(list)
        


if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    try:
        Forwarder("randomNumberGenerator", "color")
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logerr("error")
    # spin() simply keeps python from exiting until this node is stopped

        