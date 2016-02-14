#!/usr/bin/env python

import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import argparse

from oxford import Face

parser = argparse.ArgumentParser()
parser.add_argument('--image', help='Image to interact with.')
parser.add_argument('--apikey', help='Face API license key')

args = parser.parse_args()

client = Face(args.apikey)

face_lists = client.faceList.list()
for face_list in face_lists:
    if face_list['name'] == 'python-test-group':
        print "Deleting %s" % face_list
        client.faceList.delete(face_list['faceListId'])
    else:
        print "Not Deleting %s" % face_list