
import os

print("Current working directory:", os.getcwd())

import cv2


from random import randrange

from numpy import true_divide #randrange chooses a rand int in a range

executable_dir = os.path.dirname(os.path.abspath(__file__))
xml_file_path = os.path.join(executable_dir, "haarcascade_frontalcatface.xml")

cat_face_data = cv2.CascadeClassifier(xml_file_path)

#cat_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")

#cat_face_data = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
#Data comes from opencv. The Cascade Classifier function runs an algorithm on that xml file to learn to detect faces, classifier = detector
#Cascade is an algorithm type



#Image to be detected, Image is being read as a 2d array
#MeowImg = cv2.imread("meow3.jpeg")
video = cv2.VideoCapture(0) #0 means default cam, can also put file name, can also put video files in here
#Shows an image, the string is the name of window shown


while True:
    frame_read, current_frame = video.read() #First is a boolean (did it read succesfully), second is an image



#cvtColor in this instannce converts to greyscale, but can change to colour channels to dim
    current_grey_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY) #Turns blue green red to green
#Detects cat faces. Detectsd faces regardless of how big or small they are. Dected objects are returned as a list of triangles
    cat_face_coordinates = cat_face_data.detectMultiScale(current_grey_frame) #Gives a list of lists

    for i in range(len(cat_face_coordinates)):
        (x,y,h,w) = cat_face_coordinates[i] #The first index of coodonates, a 
        #(image you want a rectangle on, tuple of upper left coordonate, tuple of lower right hand coordonate, brg color, thickness)
        cv2.rectangle(current_frame, (x, y), (x+w, y+h), (0, randrange(100, 256), 0), 4)

    cv2.imshow("A renouned painter", current_frame)

    print(cat_face_coordinates)




    stop_key = stopper = cv2.waitKey(1)#waits a milisecond b4 hitting a key automatically without uer input

    if stop_key == 81 or stop_key == 113: #If key hit is q or Q
        break

