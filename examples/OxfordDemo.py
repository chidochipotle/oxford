#!/usr/bin/env python

import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import argparse
import numpy as np
import cv2

from oxford.face import Face

parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Image to interact with.')
parser.add_argument('--apikey', help='Face API license key')
parser.add_argument('--facelistid', help='Face List Id to search against')

args = parser.parse_args()

window_name = 'Oxford Demo'
img = None
faces = []

client = Face(args.apikey)

if args.facelistid is None:
    face_lists = client.faceList.list()
    face_list_id = face_lists[0]['faceListId']
else:
    face_list_id = args.facelistid
print "Face List: %s" % face_list_id

face_list = client.faceList.get(face_list_id)
print "Number of Faces: %d" % len(face_list['persistedFaces'])

def find_face(x,y):
    sx = x / width_scale
    sy = y / height_scale
    print "X: %d Y: %d -> SX: %d SY: %d" % (x, y, sx, sy)
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
        face = find_face(x, y)
        print "Face found: %s" % face['faceId']
        try:
            similar = client.similar(face['faceId'], candidateFaceListId=face_list_id)
            print similar
        except Exception as e:
            if 'FaceNotFound' in e.message:
                print "Face not found."    

        cv2.imshow(window_name, img)
             
try:
    faces = client.detect({'path': args.image})
except Exception as e:
    print e
    print "Error finding face in image (%s)." % args.image

img = cv2.imread(args.image)
img_width, img_height = img.shape[:2]

width_scale = 1024.0 / img_width
height_scale = 768.0 / img_height

resized_image = cv2.resize(img, (0,0), fx=width_scale, fy=height_scale) 

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setMouseCallback(window_name, pick)

if len(faces) == 0:
    print "Found 0 faces in image."
else:
    for face in faces:
        cv2.rectangle(resized_image, (int(face['faceRectangle']['left'] * width_scale), int(face['faceRectangle']['top'] * height_scale)), (int((face['faceRectangle']['left'] + face['faceRectangle']['width']) * width_scale), int((face['faceRectangle']['top']+ face['faceRectangle']['height']) * height_scale)), (0, 255, 255), 2)  
        print "drew face: %s" % face
        
cv2.imshow(window_name, resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()