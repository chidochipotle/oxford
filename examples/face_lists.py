#!/usr/bin/env python

import sys
import json

from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import argparse

from oxford.face import Face

parser = argparse.ArgumentParser()
parser.add_argument('--apikey', help='Face API license key')
parser.add_argument('--list', help='List facelists', action='store_true')
parser.add_argument('--info', help='Print information about facelist')
parser.add_argument('--delete', help='Delete specified facelist')
parser.add_argument('--count', help='Print the number of faces in a face list')

args = parser.parse_args()

client = Face(args.apikey)

face_lists = client.faceList.list()

if args.list:
    for face_list in face_lists:
        print json.dumps(face_list, sort_keys=True, indent=4, separators=(',', ': '))
        
if args.info:
    print json.dumps(client.faceList.get(args.info), sort_keys=True, indent=4, separators=(',', ': '))

if args.count:
    fl = client.faceList.get(args.count)
    print "There are %d faces in face list %s" % (len(fl['persistedFaces']), args.count)
    
if args.delete:
    if args.delete in face_list['faceListId']:
        print "Deleting %s" % face_list
        client.faceList.delete(args.delete)
