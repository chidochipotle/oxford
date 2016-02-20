#!/usr/bin/env python

import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import argparse
import json

from oxford.face import Face

parser = argparse.ArgumentParser()
parser.add_argument('--image', help='Image to interact with.')
parser.add_argument('--facelistid', help='Face List Id to search.')
parser.add_argument('--apikey', help='Face API license key')

args = parser.parse_args()

client = Face(args.apikey)

print "Face List ID: %s" % args.facelistid
face_list = client.faceList.get(args.facelistid)
print "Number of Faces in Face List: %d" % len(face_list['persistedFaces'])

try:
    face = client.detect({'path': args.image})[0]
    print "Face to search for:"
    print "\tFace: %s" % face['faceId']
    print "\tLocation: (Left) %d (Top) %d (Width) %d (Height) %d" % (face['faceRectangle']['left'], face['faceRectangle']['top'], face['faceRectangle']['width'], face['faceRectangle']['height'])
    left = face['faceRectangle']['left']
    right = face['faceRectangle']['left'] + face['faceRectangle']['width']
    top = face['faceRectangle']['top']
    bottom = face['faceRectangle']['top'] + face['faceRectangle']['height']

    similar = client.similar(face['faceId'], candidateFaceListId=args.facelistid)
    for possible_face in similar:
        
        print "Found Similar Face: %s Confidence: %f" % (possible_face['persistedFaceId'], possible_face['confidence'])
        face_data = [x for x in face_list['persistedFaces'] if x['persistedFaceId'] == possible_face['persistedFaceId']]
        print json.dumps(json.loads(face_data[0]['userData']), sort_keys=True, indent=4, separators=(',', ': '))
except Exception as e:
    print e
