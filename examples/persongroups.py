#!/usr/bin/env python

import sys
from os.path import abspath, dirname
sys.path.append(dirname(dirname(abspath(__file__))))

import argparse

from oxford.persongroup import PersonGroup

parser = argparse.ArgumentParser()
parser.add_argument('--apikey', help='Face API license key')

args = parser.parse_args()

persongroup = PersonGroup(args.apikey)

for group in persongroup.list():
    if group['personGroupId'] == 'pocgroup':
        print "Deleting %s" % group
        persongroup.delete(group['personGroupId'])
    else:
        print "Not Deleting %s" % group