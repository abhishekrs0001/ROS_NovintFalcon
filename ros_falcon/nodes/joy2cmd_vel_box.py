import roslib; roslib.load_manifest('ros_falcon')  
#reads the package manifest and sets up the python library path based on the package dependencies.

import rospy
#You need to import rospy if you are writing a ROS Node

from geometry_msgs.msg import Wrench
#The std_msgs.msg import is so that we can reuse the std_msgs type for publishing
from sensor_msgs.msg import Joy

def joyCallBack(data,cmd_vel):
    #print data
    print data.axes[2]
    cmd_vel.force.x = (data.axes[2]-0.1)*100
    print ("force in x:  ", cmd_vel.force.x)
    #cmd_vel.force.y = (data.axes[2]-0.1)*10000
    #cmd_vel.torque.z = data.axes[0]*-1000
    

def run():
    rospy.init_node('joy2cmd_vel', anonymous=True)
    pub_cmd_vel = rospy.Publisher('/force', Wrench, queue_size=1)
    cmd_vel = Wrench()
    sub_joy = rospy.Subscriber('/falcon/joystick', Joy, joyCallBack, cmd_vel)
    rate = rospy.Rate(15.0)
    while not rospy.is_shutdown():
        #print cmd_vel
        pub_cmd_vel.publish(cmd_vel)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException: pass
