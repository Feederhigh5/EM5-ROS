
from colors.srv import GetPosition,GetPositionResponse
import rospy

class Service:

    def __init__(self):
        service = rospy.Service('get_position', GetPosition, return_position)
        self.color = ["GREEN", "RED", "BLUE"]
        self.randomize_array()

    def return_position(req):
        return self.color.indexOf(req.color);

    def randomize_array(self):
        while not rospy.is_shutdown():
            random.shuffle(self.color)


if __name__ == '__main__':
    rospy.init_node('position_service')
