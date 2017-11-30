import numpy as np
import time
import rospy
from std_msgs.msg import Float64
count = 0
count2 = 0



# -------------------------------Ros Control
rospy.init_node('control', anonymous=False)

pub_wheel_l_f = rospy.Publisher('/path_planner/left_wheel_f_controller/command', Float64 , queue_size=10,latch=True )
pub_wheel_r_f = rospy.Publisher('/path_planner/right_wheel_f_controller/command', Float64 , queue_size=10,latch=True )
pub_wheel_l_r = rospy.Publisher('/path_planner/left_wheel_r_controller/command', Float64 , queue_size=10,latch=True )
pub_wheel_r_r = rospy.Publisher('/path_planner/right_wheel_r_controller/command', Float64 , queue_size=10,latch=True)
print 'initial publish'
pub_wheel_l_f.publish(Float64(2))
pub_wheel_r_f.publish(Float64(2))
pub_wheel_l_r.publish(Float64(2))
pub_wheel_r_r.publish(Float64(2))
time.sleep(2)



r = np.load('Route_path_2.npy')
# print r
prev_x,prev_y = r[0]
print prev_x,prev_y



for x,y in r:
    print x,y
    if (x == prev_x ):
        count = count + 1
    else:
        if (count != 0 ):
            print 'move ' + str(count) + ' steps and turn'

        if (y == prev_y ):
            count2 = count2 + 1
            print 'move ' + str(count2) + ' steps horizontally'
            pub_wheel_l_f.publish(Float64(2))
            pub_wheel_r_f.publish(Float64(2))
            pub_wheel_l_r.publish(Float64(2))
            pub_wheel_r_r.publish(Float64(2))

        elif  (y != prev_y ):
            print 'move ' + str(count2) + ' steps and turn'
            pub_wheel_l_f.publish(Float64(-1))
            pub_wheel_r_f.publish(Float64(1))
            pub_wheel_l_r.publish(Float64(-1))
            pub_wheel_r_r.publish(Float64(1))
        print count
        for k in range(count):
            print 'Publishing'
            pub_wheel_l_f.publish(Float64(2))
            pub_wheel_r_f.publish(Float64(2))
            pub_wheel_l_r.publish(Float64(2))
            pub_wheel_r_r.publish(Float64(2))


        prev_x = x
        prev_y = y
        count = 0
        count2 = 0


# print 'move ' + str(count) + ' steps and turn'
