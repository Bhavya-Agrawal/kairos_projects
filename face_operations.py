#!/usr/bin/python3

import kairos_face
import json
import requests

kairos_face.settings.app_id = "2b0335d7"
kairos_face.settings.app_key = "28e7a2915e876413a7f33b2eccd06a62"

options ='''
1. enroll
2. detect
3. recognize
'''

print(options)
op = input("give the appropriate option\n")

location = input("enter the image path\n")
#identity = input("enter the id\n")
#gallery = input("enter the gallery name\n")

try:
	# for enrolling
	if op == "1":
		# enrolling  a face from gallery or the website
		# Enrolling from a file
		# each input is the string
		enrolled_face = kairos_face.enroll_face(file=location, subject_id='student', gallery_name='Demo')
		print(enrolled_face)

	# for detecting
	elif op == "2":
		'''url = "https://api.kairos.com/detect"

		headers = {
   	 	"app_id": "2b0335d7",
    	"app_key": "28e7a2915e876413a7f33b2eccd06a62"
		}

		# Detect from a file
		files= {'image':open(location,'rb')}

		r = requests.post(url, files=files, headers=headers)
		print(r.text)'''

		# Detect from a file
		detected_faces = kairos_face.detect_face(file=location)
		print(detected_faces)

	# for recognizing image	
	elif op == "3":
		# Recognizing from a file
		recognized_faces = kairos_face.recognize_face(file=location, gallery_name='Demo')
		print(recognized_faces)

		#load and read string type data from json file
		#data = json.loads(recognized_faces)

		# read dictionary type data into str type data
		# now data is in the form of string so can apply .loads() method to it
		data = json.dumps(recognized_faces)
		#print(type(data))

		# reading from data now
		dic_data = json.loads(data)
		#json.loads() take str as input and returns dictionary  
		#print(str_data)
	

		# reading specific value from json dictionary str_data using key values
		# to read complete images
		out = dic_data['images']
		print(type(out))

		#to read transaction of 1st face and its corresponding status from images
		status = out[0]['transaction']['status']
		cand = out[0]['candidates']
		#out = dic_data['images']['transaction']['confidence']
		#print(status)
		#print(type(cand))
		#print(cand)
		# to print list from list 
		print(cand[0]['enrollment_timestamp'])
		print(cand)

		# read all the above data in just 1 line from the obtained json array
		print(dic_data['images'][0]['transaction']['status'])
		#print(dic_data['images'][0][['candidates'['confidence']]])

except FileNotFoundError:
	print("the desired file is not found")	







