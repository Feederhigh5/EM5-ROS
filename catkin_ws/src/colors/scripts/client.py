
import sys
import rospy

from colors.srv import *

class Client:

    def __init__(self, color):
        self.color = color

    @staticmethod
    def get_position(color):
        rospy.wait_for_service('get_position')
        try:
            get_position = rospy.ServiceProxy('get_position', GetPosition)
            response = get_position(color)
            return response
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)


if __name__ == "__main__":
    client=Client("RED")
    print("Requesting %s"%client.color)
    print("%s in Position %s"%(client.color, client.get_position(client.color)))