#!/usr/bin/python3

import kairos_face
import json
import mysql.connector as mysql
import cv2
import requests


# credentials for kairos
kairos_face.settings.app_id = "2b0335d7"
kairos_face.settings.app_key = "28e7a2915e876413a7f33b2eccd06a62"

location = ""

# instance for image capture
cam = cv2.VideoCapture(0)


# create a connection with database
conn = mysql.connect(user='bhavya',password='Bhavya1910',database='Enroll_Images',host='localhost')
cursor = conn.cursor()

#check the connection with database
if conn.is_connected():
	print("Database Connection is established")
else:
	print("sorry database not connected,check your connection once")	


def recognize_image(path):
	recognized_image = kairos_face.recognize_face(file=path,gallery_name='Demo')
	print(recognized_image)
	data = json.dumps(recognized_image)

	# for dict from data
	dic_data = json.loads(data)  

	# getting status out of data
	status = (dic_data['images'][0]['transaction']['status'])

	enroll(status,path)



def enroll_image(location,sub_id):
	print(location)
	print(type(sub_id))
	print(sub_id)
	enrolled_face = kairos_face.enroll_face(file=location, subject_id=str(sub_id), gallery_name='Demo')
	print(enrolled_face)



def enroll(status,path):
	# check if the image is already enrolled or not
	if status == 'success':
		print("image is already registered,go to attendence system to mark your attendence")

	elif status == 'failure':
		print("your image is not registered,enter the details and take a picture of yours")
		register(path)

	else:
		print("sorry not a valid picture")


def register(path):
	location = path
	Name = input("Enter your name\n")
	Contact = input("enter your contactno\n")
	Branch = input("enter your branch\n")

	# enter into the database
	cursor.execute("INSERT INTO Images (name,branch,contactno) VALUES (%s,%s,%s)", (Name,Branch,Contact));
	conn.commit()

	cursor.execute("SELECT * FROM Images")
	out = cursor.fetchall()
	#print(out)
	#print(type(out))

	for i in out:
		if i[3] == Contact:
			#print(i[0])
			sub_id = i[0]

	if sub_id ==  "":
		sub_id = 1

	# now to take a picture
	print("your details have been registered,please give a picture now\n")
	status,frame = cam.read()
	cv2.imshow("pic",frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		cam.release()

	cv2.imwrite("./Take_Images/"+str(sub_id)+".png",frame)

	enroll_image(location,sub_id)



if __name__=="__main__":
	try:
		# give the path of image
		path = input("enter the path of your image\n")
		recognize_image(path)

	except FileNotFoundError:
		print("sorry invalid path entered by you")	













