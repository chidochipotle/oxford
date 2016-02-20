#!/usr/bin/env python

import os
import argparse
import json
import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('load_faces.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

from oxford.face import Face
from oxford.person import Person
from oxford.facelist import FaceList

parser = argparse.ArgumentParser()
parser.add_argument('--source', required=True,
                    help='Directory of images or a single image to load.')
parser.add_argument('--apikey', required=True, help='Face API license key')
parser.add_argument('--facelist', help='Basename for facelist.', default='facelist')
parser.add_argument('--dryrun', action='store_true')

args = parser.parse_args()

facelist = FaceList(args.apikey)
face = Face(args.apikey)

facelist_count = 0
facelist_id = "%s-%d" % (args.facelist, facelist_count)
facelist_name = "Face List %d" % facelist_count
facelist_count += 1

try:
    logger.info("Making facelist.")
    facelist.create(facelist_id, facelist_name)
    logger.info("Finished making facelist.")
except Exception as e:
    logger.error("Problem creating facelist: %s" % e)
    
face_result = []
if os.path.exists(args.source):
    if os.path.isdir(args.source):
        for dirName, subdirList, fileList in os.walk(args.source):
            if len(fileList) != 0 and len(subdirList) == 0:
                faces = []
                for fname in fileList:
                    if(fname not in [".DS_Store"]):
                        fpath = os.path.realpath(os.path.join(dirName, fname))
                        try:
                            face_result = face.detect({'path': fpath})
                            logger.info("Got faces (%d) for image %s." % (len(face_result), fname))
                        except Exception as e:
                            logger.error("Error %s finding face in image (%s)." % (e, fpath))
                        
                        # TODO: If face list doesn't have enough room for all the faces, make a new one and keep track of the names
                        if len(face_result) > 0:
                            for face_found in face_result:
                                target_face = "%s,%s,%s,%s" % (face_found['faceRectangle']['left'], face_found['faceRectangle']['top'], face_found['faceRectangle']['width'], face_found['faceRectangle']['height'])
                                user_data = json.dumps({'file': fname, 'faceRectangle':face_found['faceRectangle']})
                                try:
                                    facelist.addFace(facelist_id, {'path':fpath}, targetFace=target_face, userData=user_data)
                                    logger.info("Added face %s (%s, %s) to %s" % (face_found, target_face, user_data, facelist_id))
                                except Exception as e:
                                  logger.error("Error %s adding face (%s)." % (e, user_data))
                        
    elif os.path.isfile(args.source):
        fpath = os.path.realpath(args.load)
        try:
            face_result = face.detect({'path': fpath})
        except Exception as e:
            logger.error("Error finding face in image (%s)." % fpath)
        if len(face_result) > 0:
            faces.append(face_result[0]['faceId'])

        logger.info("Adding faces to %s (%s)." % (person_name, ", ".join(faces)))
        person.create(args.persongroup, faces,person_name)

logger.info("Training person group.")
# person_group.trainAndPollForCompletion(args.persongroup)

logger.info("Done training person group, ready for testing.")
# person_group.delete(args.persongroup)