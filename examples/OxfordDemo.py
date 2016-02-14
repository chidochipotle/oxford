#!/usr/bin/env python

import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import argparse
import numpy as np
import cv2

from oxford import Client

parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Image to interact with.')
parser.add_argument('--apikey', help='Face API license key')

args = parser.parse_args()

window_name = 'Oxford Demo'
img = None
faces = []

client = Client.Client()

face_lists = client.face(args.apikey).faceList.list()

face_list_id = face_lists[0]['faceListId']
print "Face List: %s" % face_list_id

face_list = client.face(args.apikey).faceList.get(face_list_id)
print "Number of Faces: %d" % len(face_list['persistedFaces'])

def find_face(x,y):
    for face in faces:
        left = face['faceRectangle']['left']
        right = face['faceRectangle']['left'] + face['faceRectangle']['width']
        top = face['faceRectangle']['top']
        bottom = face['faceRectangle']['top'] + face['faceRectangle']['height']
 
        if x > left and x < right and y > top and y < bottom:
            return face
            
    return None
        
def pick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        face = find_face(x,y)
        print "Face found: %s" % face['faceId']
        try:
            similar = client.face(args.apikey).similar(face['faceId'], candidateFaceListId=face_list_id)
            print similar
        except Exception as e:
            if 'FaceNotFound' in e.message:
                print "Face not found."    

        cv2.imshow(window_name, img)
             
try:
    faces = client.face(args.apikey).detect({'path': args.image})
except Exception as e:
    print e
    print "Error finding face in image (%s)." % args.image

img = cv2.imread(args.image)
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setMouseCallback(window_name, pick)

if len(faces) == 0:
    print "Found 0 faces in image."
else:
    for face in faces:
        cv2.rectangle(img, (face['faceRectangle']['left'], face['faceRectangle']['top']), (face['faceRectangle']['left'] + face['faceRectangle']['width'], face['faceRectangle']['top']+ face['faceRectangle']['height']), (0, 255, 255), 2)  

cv2.imshow(window_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()