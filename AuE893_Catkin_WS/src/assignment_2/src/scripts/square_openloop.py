#!/usr/bin/env python
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi

def move_square():
    rospy.init_node('turtlebot_controller', anonymous=True)

    # Create a publisher which can "talk" to Turtlesim and tell it to move
    velocity_publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
     
    # Create a Twist message and add linear x and angular z values
    linear_vel = Twist()
    angular_vel= Twist()
    linear_vel.linear.x = 0.2
    angular_vel.angular.z = 0.2

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        current_angle=0
        i=0


        while(i<4):
            #Loop to move the turtle in an specified distance
            while(current_distance < 2):
                #Publish the velocity
                velocity_publisher.publish(linear_vel)
                #Takes actual time to velocity calculus
                t1=rospy.Time.now().to_sec()
                #Calculates distancePoseStamped
                current_distance= 0.2*(t1-t0)
            #After the loop, stops the robot
            linear_vel.linear.x = 0
            velocity_publisher.publish(linear_vel)
            t0=rospy.Time.now().to_sec()
            while(current_angle < pi/2):
                velocity_publisher.publish(angular_vel)
                t1=rospy.Time.now().to_sec()
                current_angle= 0.2*(t1-t0)
            angular_vel.angular.z=0
            velocity_publisher.publish(angular_vel)
            t0=rospy.Time.now().to_sec()
            current_distance = 0
            current_angle=0
            i=i+1
            linear_vel.linear.x = 0.2
            angular_vel.angular.z = 0.2    


if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass

