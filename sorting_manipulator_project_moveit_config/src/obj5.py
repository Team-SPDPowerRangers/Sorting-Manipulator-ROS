#!/usr/bin/env python3

 

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg._JointTrajectoryPoint import JointTrajectoryPoint
import time
from colorDetect import detect_color
from std_msgs.msg import String

 

def sort_object(lift, pick, obj_num):
    global move_pub, move_pub_gripper, arm_cmd,gripper_cmd, joint_point, gripper_joint_point
    global green_place_list,red_place_list,blue_place_list
    ## obj_1_lift
    joint_point.positions = lift
    arm_cmd.points = [joint_point]
    move_pub.publish(arm_cmd)
    print('Message Published!!! : Moved to obj_'+obj_num+'_lift')
    time.sleep(4)
    ## obj_1_pick
    joint_point.positions = pick
    arm_cmd.points = [joint_point]
    move_pub.publish(arm_cmd)
    print('Message Published!!! : Moved to obj_'+obj_num+'_pick')
    time.sleep(4)
    ## gripper_close
    gripper_joint_point.positions = [0.0150, -0.0150]
    gripper_cmd.points = [gripper_joint_point]
    move_pub_gripper.publish(gripper_cmd)
    print('Message Published!!! : Object gripped')
    time.sleep(4)

 

                    ##### COLOR IDENTIFICATION #####
    #global value
    def callBack(msg):
        global value
        value=msg.data

 

    detect_color()
    sub=rospy.Subscriber("block_color", String,callBack)
    rospy.wait_for_message("block_color",String)
    print("Object color detected : ",value)

 

    place=[]
    if value=='GREEN':
        place=green_place_list[int(obj_num)]
    elif value=='BLUE':
        place=blue_place_list[int(obj_num)]
    else:
        place=red_place_list[int(obj_num)]

 

    ## obj_1_lift
    joint_point.positions = lift
    arm_cmd.points = [joint_point]
    move_pub.publish(arm_cmd)
    print('Message Published!!! : Moved to obj_'+obj_num+'_lift')
    time.sleep(4)
    ## green_obj_place_better
    joint_point.positions = place
    arm_cmd.points = [joint_point]
    move_pub.publish(arm_cmd)
    print('Message Published!!! : Moved to '+value+'_obj_place')
    time.sleep(4)
    ## gripper_open
    gripper_joint_point.positions = [0.0000, -0.0000]
    gripper_cmd.points = [gripper_joint_point]
    move_pub_gripper.publish(gripper_cmd)
    print('Message Published!!! : Object released')
    time.sleep(4)
    ## initial
    joint_point.positions = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
    arm_cmd.points = [joint_point]
    move_pub.publish(arm_cmd)
    print('Message Published!!! : Moved to Initial position')
    time.sleep(4)
    print('########## OBJECT-'+obj_num+' DONE ##########')
        
        

 

def move():
    global move_pub, move_pub_gripper

 

    move_pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=1, latch=True)
    move_pub_gripper = rospy.Publisher('/gripper_controller/command', JointTrajectory, queue_size=1, latch=True)
    rospy.init_node('arm_move', anonymous=True)
    
    global arm_cmd, gripper_cmd
    arm_cmd = JointTrajectory()
    gripper_cmd = JointTrajectory()

 

    ## ARM    
    arm_cmd.joint_names = ["joint1", "joint2", "joint3", "joint4", "joint5", "joint6"]
    ## GRIPPER
    gripper_cmd.joint_names = ["f_joint1", "f_joint2"]
    
    global joint_point, gripper_joint_point
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

 


 
    sort_object(obj_5_lift,obj_5_pick,'2')
 
    
    print('\n########## EXECUTION DONE ##########\n')

 

    

 

global gripper_open,gripper_mid,gripper_close
global obj_1_lift,obj_2_lift,obj_3_lift,obj_4_lift,obj_5_lift,obj_6_lift,obj_7_lift,obj_8_lift,obj_9_lift
global obj_1_pick,obj_2_pick,obj_3_pick,obj_4_pick,obj_5_pick,obj_6_pick,obj_7_pick,obj_8_pick,obj_9_pick 
global green_obj_place_1,green_obj_place_2,green_obj_place_3,red_obj_place_1,red_obj_place_2,red_obj_place_3,blue_obj_place_1,blue_obj_place_2,blue_obj_place_3
global green_place_list,red_place_list,blue_place_list
gripper_open=[0.0000, 0.0000]
gripper_mid=[0.0100, -0.0100]
gripper_close=[0.0150, -0.0150]
initial=[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]
obj_1_lift=[0.0000, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_2_lift=[0.3925, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_3_lift=[0.7850, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_4_lift=[1.5700, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_5_lift=[2.3550, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_6_lift=[3.1400, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_7_lift=[-2.3550, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_8_lift=[-1.5700, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_9_lift=[-0.7850, -0.5465, 1.1564, 0.0000, 1.1500, 0.0000]
obj_1_pick=[0.0000, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_2_pick=[0.3925, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_3_pick=[0.7850, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_4_pick=[1.5700, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_5_pick=[2.3550, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_6_pick=[3.1400, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_7_pick=[-2.3550, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_8_pick=[-1.5700, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
obj_9_pick=[-0.7850, 0.0607, 1.7465, 0.0000, 1.3489, 0.0000]
green_obj_place_1=[0.7850, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
red_obj_place_1=[2.3550, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
blue_obj_place_1=[-1.9625, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
green_obj_place_2=[0.8500, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
red_obj_place_2=[2.4200, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
blue_obj_place_2=[-2.0275, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
green_obj_place_3=[0.9150, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
red_obj_place_3=[2.2900, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]
blue_obj_place_3=[-1.8975, 1.0149, 0.2414, 0.0000, 1.7749, 0.0000]    
green_place_list=[[],green_obj_place_1,green_obj_place_2,green_obj_place_3]
red_place_list=[[],red_obj_place_1,red_obj_place_2,red_obj_place_3]
blue_place_list=[[],blue_obj_place_1,blue_obj_place_2,blue_obj_place_3]
    

 

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
