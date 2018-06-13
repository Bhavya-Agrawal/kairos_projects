#!/usr/bin/python3

import cv2
import enroll_images

cam = cv2.VideoCapture(0)


if cam.isOpened():
	print("opened")

def pic():
#writing this image in a local gallery of system
	while cam.isOpened():
		status,frame = cam.read()
		cv2.imshow("image",frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.imwrite("./Take_Images/image.png",frame)
			cv2.destroyAllWindows()
			cam.release()
	give_image("./Take_Images/image.png")


def give_image(path):
	enroll_images.recognize_image(path)

pic()	

