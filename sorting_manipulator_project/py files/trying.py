#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String
bridge = CvBridge()
def detect_callback(image_msg, color_pub):
    # for i in range(2):
        # possible_colors = [[[17,15,100],[50,56,200]],[[25, 146, 190], [62, 174, 250]]]
        # possible_colors = [[[200,0,0],[255,125,125]],[[0,200,0],[125,255,125]],[[0,0,200],[125,125,255]]]
        # possible_colors = [[116,14,14],[14,116,14],[14,14,116]]
        #possible_colors = [[102, 0, 0],[0, 102, 0],[0, 0, 102]]
        possible_colors = [[127,25,25],[25,127,25],[25,25,127]] 
        global once
        try:
            BLUE = 'BLUE'
            GREEN = 'GREEN'
            RED = 'RED'
            cv_image = bridge.imgmsg_to_cv2(image_msg, 'bgr8')
            # cv2.imshow("ImageFrame",im)
            # print("Image : {0} \n Size : {1}".format(cv_image[0], cv_image.shape))
            x = cv_image.tolist()
            color_found = []
            # print("Image : {0}".format(i) for i in x if (i[0]<50 or i[1]<50 or i[2]<50) )

            hurray = False
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
                        # print('BLUE')
                        color_found.append(BLUE)
                    elif green == 3:
                        color_found.append(GREEN)
                        # print('GREEN')
                    elif red == 3:
                        color_found.append(RED)
                        # print('RED')
                    count_vaues = [color_found.count(BLUE), color_found.count(GREEN), color_found.count(RED)]
                    max_val = max(count_vaues)
                    if max_val > 5500:
                        print(count_vaues)
                        colors = [BLUE, GREEN, RED]
                        val = max(range(len(colors)), key=lambda i: count_vaues[i])
                        hurray = True
                        if once:
                            once = False
                            color_pub.publish(colors[val])
                        return
                if hurray:
                    return
            color_pub.publish('NONE')
            # subs.unregister()
            # print(color_found.count('BLUE'), color_found.count('GREEN'), color_found.count('RED'))
            
        except CvBridgeError as e:
            print(e)
        

def detect_color():
    global once
    once = True
    color_pub = rospy.Publisher("block_color", String, queue_size = 1)
    subs = rospy.Subscriber('/mybot/camera1/image_raw', Image, detect_callback, color_pub)
    rospy.Rate(1)
    # cam_topic = '/mybot/camera1/image_raw'
    # subs = rospy.Subscriber(rospy.get_param('/mybot/camera1/image_raw'), Image, detect_callback)

if __name__ == '__main__':
    try:
        rospy.init_node('block_color_identifier', anonymous=True)
        detect_color()
    except rospy.ROSInternalException:
        pass

        '''
        #!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

bridge = CvBridge()

def detect_callback(image_msg):
    # for i in range(2):

        # possible_colors = [[[17,15,100],[50,56,200]],[[25, 146, 190], [62, 174, 250]]]
        # possible_colors = [[[200,0,0],[255,125,125]],[[0,200,0],[125,255,125]],[[0,0,200],[125,125,255]]]
        #possible_colors = [[116,14,14],[14,116,14],[14,14,116]]
        possible_colors = [[127,25,25],[25,127,25],[25,25,127]]

        try:
            cv_image = bridge.imgmsg_to_cv2(image_msg, 'bgr8')
            # cv2.imshow("ImageFrame",im)
            # print("Image : {0} \n Size : {1}".format(cv_image[0], cv_image.shape))
            x = cv_image.tolist()

            color_found = []


            
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
                            color_found.append('BLUE')
                        elif green == 3:
                            color_found.append('GREEN')
                        elif red == 3:
                            color_found.append('RED')
                        
                        



            # print("Image : {0} \n Size : {1}".format(x, len(x)))
            # print(type(x))
            print("Final Color: ",color_found)
        except CvBridgeError as e:
            print(e)

        


def detect_color():

    
       rospy.init_node('block_color_identifier', anonymous=True)
       rospy.Subscriber('/mybot/camera1/image_raw', Image, detect_callback)
       rospy.spin()


if __name__ == '__main__':
    try:
        detect_color()
    except rospy.ROSInternalException:
        pass


'''