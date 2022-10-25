
import sys
import rospy

import colors.srv import *

def get_position(color):
    rospy.wait_for_service('get_position')
    try:
        get_position = rospy.ServiceProxy('get_position', GetPosition)
        response = get_position(color)
        return response
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == "__main__":
    print("Requesting %s"%color)
    print("%s in Position %i"(color, get_position(color)))