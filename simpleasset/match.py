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
    "JS": [
        "text/javascript"
    ],
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


def process_ext(mimeext, ext, text, clas):
    "Processes part based on extension"

    mime = mimeext["mime"]
    filt = config.ASSET_FILTERS.get(mime, None)
    ext = mimeext.get("ext", None if filt else ext)

    if filt:
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

    return (ext, text, clas)


def process(fname, text, clas=""):
    "Processes document based on matched rules"
    lst = fname.split(".")
    for pos in reversed(range(1, len(lst))):
        mimeext = config.ASSET_EXTS.get(lst[pos], None)
        if mimeext:
            (lst[pos], text, clas) = process_ext(mimeext, lst[pos], text, clas)

    fname = ".".join([lst[0]] + [ext for ext in lst[1:] if ext])
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
    # TODO: This is very bad, need to handle only leading directory name
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

    onlyfiles = [f for f in os.listdir(source) if isfile(join(source, f))]
    for fil in onlyfiles:
        oname = join(source, fil)

        try:
            (fname, text, clas) = process_file(oname, source, dest) # pylint: disable=W0612
            res.append((True, oname, fname))
        except AssetException as exc:
            res.append((False, oname, str(exc)))

    return res

