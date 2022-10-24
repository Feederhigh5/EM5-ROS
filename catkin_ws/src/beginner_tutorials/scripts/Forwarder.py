#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Num

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
    except rospy.ROSInterruptException
    # spin() simply keeps python from exiting until this node is stopped

        