"""
SimpleAsset rule matcher
"""

from __future__ import unicode_literals

import errno
import os
from os.path import isfile, join
from subprocess import PIPE, Popen

from simpleasset import AssetException, config, filters
from simpleasset.compat import * # pylint: disable=W0401

ASSET_CLASSES = {
    "": [
        "text/generictemplate",
        "text/jinja2"
    ],
    "JS": [],
    "CSS": []
}


def make_sure_path_exists(path):
    "Ensures a path exists"

    path = os.path.dirname(path)
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def process(fname, text, clas=""):
    "Processes document based on matched rules"

    mime = config.ASSET_EXTS.get(fname.split(".")[-1], None)
    while mime:
        filt = config.ASSET_FILTERS[mime]

        if filt['type'] == "python":
            try:
                fun = getattr(filters, filt['func'])
            except AttributeError:
                raise AssetException("Filter %s not available." % filt['func'])
            text = fun(text, config.ASSET_CONTEXT)

        elif filt['type'] == "pipe":
            proc = Popen(filt['args'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
            newtext, err = proc.communicate(text.encode('utf-8'))
            if proc.returncode == 0:
                text = bytes(newtext).decode('utf-8')
            else:
                raise AssetException("Pipe failed with status code %d\n%s" % (proc.returncode, err))
        else:
            raise AssetException("Type %s not understood." % filt['type'])

        fname = ".".join(fname.split(".")[:-1])
        mime = config.ASSET_EXTS.get(fname.split(".")[-1], None)
    return (fname, text, clas)


def process_file(oname, source, dest):
    "Processes a file through process()"

    # Read file
    try:
        ifl = open(oname)
    except FileNotFoundError:
        raise AssetException("File %s not found" % oname)
    text = ifl.read()
    ifl.close()

    # Process
    (fname, text, clas) = process(oname, text)

    # rename directory
    # TODO: This is very bad
    fname = fname.replace(source, dest)

    # Write file
    make_sure_path_exists(fname)
    ofl = open(fname, "w")
    ofl.write(text)
    ofl.close()

    return (fname, text, clas)

def process_dir(source, dest):
    "Process a directory"

    res = []

    onlyfiles = [ f for f in os.listdir(source) if isfile(join(source, f)) ]
    for fil in onlyfiles:
        oname = join(source, fil)

        try:
            (fname, text, clas) = process_file(oname, source, dest) # pylint: disable=W0612
            res.append((True, oname, fname))
        except AssetException as exc:
            res.append((False, oname, str(exc)))

    return res

