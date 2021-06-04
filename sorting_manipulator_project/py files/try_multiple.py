#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg._JointTrajectoryPoint import JointTrajectoryPoint
import time

def move():
	move_pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=1, latch=True)
	move_pub_gripper = rospy.Publisher('/gripper_controller/command', JointTrajectory, queue_size=1, latch=True)
	rospy.init_node('arm_move', anonymous=True)
	
	arm_cmd = JointTrajectory()
	gripper_cmd = JointTrajectory()

	## ARM	
	arm_cmd.joint_names = ["joint1", "joint2", "joint3", "joint4", "joint5", "joint6"]
	## GRIPPER
	gripper_cmd.joint_names = ["f_joint1", "f_joint2"]
	## ARM
	joint_point = JointTrajectoryPoint()
	## GRIPPER
	gripper_joint_point = JointTrajectoryPoint()

	## ARM
	joint_point.velocities = []
	joint_point.accelerations = []
	joint_point.effort = []
	joint_point.time_from_start = rospy.rostime.Duration(secs=1, nsecs=0)

	## GRIPPER
	gripper_joint_point.velocities = []
	gripper_joint_point.accelerations = []
	gripper_joint_point.effort = []
	gripper_joint_point.time_from_start = rospy.rostime.Duration(secs=1, nsecs=0)
	gripper_cmd.points = [gripper_joint_point]

	
	## obj_1_lift
	joint_point.positions = [0.0000, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]		
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_1_lift')
	time.sleep(3)
	## obj_1_pick
	joint_point.positions = [0.0000, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_1_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_1_lift
	joint_point.positions = [0.0000, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]		
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_1_lift')
	time.sleep(3)
	## green_obj_place
	joint_point.positions = [0.7850, 0.8761, 0.2414, 0.0000, 1.5193, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to green_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-1 DONE ##########')


	## obj_2_lift
	joint_point.positions = [0.3925, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_2_lift')
	time.sleep(3)
	## obj_2_pick
	joint_point.positions = [0.3925, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_2_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_2_lift
	joint_point.positions = [0.3925, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_2_lift')
	time.sleep(3)
	## blue_obj_place
	joint_point.positions = [-2.3550, 0.8761, 0.2414, 0.0000, 1.5193, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to blue_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-2 DONE ##########')

	## obj_3_lift
	joint_point.positions = [0.7850, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_3_lift')
	time.sleep(3)
	## obj_3_pick
	joint_point.positions = [0.7850, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_3_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_3_lift
	joint_point.positions = [0.7850, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_3_lift')
	time.sleep(3)
	## red_obj_place
	joint_point.positions = [2.3550, 0.8761, 0.2414, 0.0000, 1.5193, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to red_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-3 DONE ##########')






	## obj_4_lift
	joint_point.positions = [1.5700, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_4_lift')
	time.sleep(3)
	## obj_4_pick
	joint_point.positions = [1.5700, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_4_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_4_lift
	joint_point.positions = [1.5700, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_4_lift')
	time.sleep(3)
	## blue_obj_place_better_2
	joint_point.positions = [-1.9400, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to blue_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-4 DONE ##########')


	## obj_5_lift
	joint_point.positions = [2.3550, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_5_lift')
	time.sleep(3)
	## obj_5_pick
	joint_point.positions = [2.3550, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_5_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_5_lift
	joint_point.positions = [2.3550, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_5_lift')
	time.sleep(3)
	## red_obj_place_better_2
	joint_point.positions = [2.3900, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to red_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-5 DONE ##########')

	## obj_6_lift
	joint_point.positions = [3.1400, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_6_lift')
	time.sleep(3)
	## obj_6_pick
	joint_point.positions = [3.1400, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_6_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_6_lift
	joint_point.positions = [3.1400, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_6_lift')
	time.sleep(3)
	## green_obj_place_better_2
	joint_point.positions = [0.8500, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to green_obj_place')
	time.sleep(3)	
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-6 DONE ##########')






	## obj_7_lift
	joint_point.positions = [-2.3550, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_7_lift')
	time.sleep(3)
	## obj_7_pick
	joint_point.positions = [-2.3550, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_7_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_7_lift
	joint_point.positions = [-2.3550, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_7_lift')
	time.sleep(3)
	## blue_obj_place_better_3
	joint_point.positions = [-1.9000, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to blue_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-7 DONE ##########')


	## obj_8_lift
	joint_point.positions = [-1.5700, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_8_lift')
	time.sleep(3)
	## obj_8_pick
	joint_point.positions = [-1.5700, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_8_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_8_lift
	joint_point.positions = [-1.5700, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_8_lift')
	time.sleep(3)
	## green_obj_place_better_3
	joint_point.positions = [0.9000, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to green_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-8 DONE ##########')

	## obj_9_lift
	joint_point.positions = [-0.7850, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_9_lift')
	time.sleep(3)
	## obj_9_pick
	joint_point.positions = [-0.7850, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_9_pick')
	time.sleep(3)
	## gripper_close
	gripper_joint_point.positions = [0.0150, -0.0150]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object gripped')
	time.sleep(3)
	## obj_9_lift
	joint_point.positions = [-0.7850, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to obj_9_lift')
	time.sleep(3)
	## red_obj_place_better_3
	joint_point.positions = [2.4200, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to red_obj_place')
	time.sleep(3)
	## gripper_open
	gripper_joint_point.positions = [0.0000, -0.0000]
	gripper_cmd.points = [gripper_joint_point]
	move_pub_gripper.publish(gripper_cmd)
	print('Message Published!!! : Object released')
	time.sleep(3)
	## initial
	joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
	arm_cmd.points = [joint_point]
	move_pub.publish(arm_cmd)
	print('Message Published!!! : Moved to Initial position')
	time.sleep(3)
	print('########## OBJECT-9 DONE ##########')
	print('\n########## EXECUTION DONE ##########\n')


if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:
		pass