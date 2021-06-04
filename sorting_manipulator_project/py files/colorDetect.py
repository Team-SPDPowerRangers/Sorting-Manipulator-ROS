
#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String

bridge = CvBridge()

def detect_callback(image_msg, color_publisher):    
        possible_colors = [[127,25,25],[25,127,25],[25,25,127]]
        global onely_once
        try:
            BLUE = 'BLUE'
            GREEN = 'GREEN'
            RED = 'RED'
            cv_image = bridge.imgmsg_to_cv2(image_msg, 'bgr8')            
            x = cv_image.tolist()
            color_found = []            

            correct = False
            row = len(x)
            for i in range(row):                
                col = len(x[i])
                for j in range(col):
                    blue, green, red = 0,0,0
                    for k in range(3):
                        if x[i][j][k] == possible_colors[0][k]:
                            blue = blue + 1
                        if x[i][j][k] == possible_colors[1][k]:
                            green = green + 1
                        if x[i][j][k] == possible_colors[2][k]:
                            red = red + 1
                    
                    if blue == 3:                        
                        color_found.append(BLUE)
                    elif green == 3:
                        color_found.append(GREEN)                        
                    elif red == 3:
                        color_found.append(RED)
                    count_vaues = [color_found.count(BLUE), color_found.count(GREEN), color_found.count(RED)]
                    max_val = max(count_vaues)                    
                    if max_val > 3500:
                        #print(count_vaues)
                        colors = [BLUE, GREEN, RED]
                        val = max(range(len(colors)), key=lambda i: count_vaues[i])
                        correct = True
                        if onely_once == 0:
                            onely_once += 1
                        elif onely_once == 1:
                            onely_once += 1
                            color_publisher.publish(colors[val])
                        break
                if correct:
                    return           
            
        except CvBridgeError as e:
            print(e)
        

def detect_color():
    global onely_once
    onely_once = 0    
    color_publisher = rospy.Publisher("block_color", String, queue_size = 1)
    subs = rospy.Subscriber('/mybot/camera1/image_raw', Image, detect_callback, color_publisher)
    rospy.Rate(2)    

if __name__ == '__main__':
    try:
        rospy.init_node('block_color_identifier', anonymous=True)    
        detect_color()
    except rospy.ROSInternalException:
        pass
 