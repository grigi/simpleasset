#!/usr/bin/env python
"""
Asset Generator
"""

import argparse

from simpleasset import config, process_dir
from simpleasset.config_container import DEFAULT_CONFIG

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
    res = process_dir(source, dest)
    print("Source: %s -> %s\n%d Files processed" % (source, dest, len(res)))
    for item in res:
        print("%s: %s%s %s" % ('Ok' if item[0] else 'Error', item[1], ' ->' if item[0] else ':', item[2]))
