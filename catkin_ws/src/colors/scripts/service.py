

class Service:

    def __init__(self):
        service = rospy.Service('give_position', GivePosition, return_position)


    def return_position():
        

if __name__ == '__main__':
    rospy.init_node('position_service')
