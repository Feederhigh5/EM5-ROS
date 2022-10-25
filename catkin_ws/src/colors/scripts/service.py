
from colors.srv import GetPosition,GetPositionResponse
import rospy
import random

class Service:

    def __init__(self):
        service = rospy.Service('get_position', GetPosition, self.return_position)
        self.colors = ["GREEN", "RED", "BLUE"]
        self.randomize_array()
        rospy.loginfo("array %s"%self.colors)

    def return_position(self, req):
        rospy.loginfo('Returning position of %s in %s'%(req.color, self.colors))
        pos = self.colors.index(req.color)+1;
        return GetPositionResponse(pos)

    def randomize_array(self):
        # while not rospy.is_shutdown():
        random.shuffle(self.colors)


if __name__ == '__main__':
    rospy.init_node('position_service')
    Service()
    rospy.spin()