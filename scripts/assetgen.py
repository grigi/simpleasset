#!/usr/bin/env python
"""
Asset Generator
"""

import argparse
from os import listdir
from os.path import isfile, join

from simpleasset import AssetException, config
from simpleasset.config_container import DEFAULT_CONFIG
from simpleasset.match import process_file

parser = argparse.ArgumentParser(description='Asset Generator')
parser.add_argument('-c', '--config',
    dest='config_file',
    type=str,
    default=DEFAULT_CONFIG,
    help='Specify configuration file'
    )

args = parser.parse_args()
config.load(args.config_file)

for a in config.ASSET_SOURCES:
    source = a['in']
    dest = a['out']
    print("Source:\t%s\nDest:\t%s" % (source, dest))

    onlyfiles = [ f for f in listdir(source) if isfile(join(source, f)) ]
    for fil in onlyfiles:
        oname = join(source, fil)

        try:
            (fname, text, clas) = process_file(oname)
            print("%s -> %s" % (oname, fname))
        except AssetException as exc:
            print(exc)
