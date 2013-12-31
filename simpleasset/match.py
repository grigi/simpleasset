import errno
import os

from simpleasset import AssetException, config, filters

ASSET_CLASSES = {
    "": [
        "text/generictemplate",
        "text/jinja2"
    ],
    "JS": [],
    "CSS": []
}


def make_sure_path_exists(path):
    path = os.path.dirname(path)
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def process(fname, text, clas=""):
    mime = config.ASSET_EXTS.get(fname.split(".")[-1], None)
    while mime:
        filt = config.ASSET_FILTERS[mime]

        if filt['type'] == "python":
            try:
                fun = getattr(filters, filt['func'])
            except AttributeError:
                raise AssetException("Filter %s not available." % filt['func'])
            text = fun(text, config.ASSET_CONTEXT)
            fname = ".".join(fname.split(".")[:-1])

        elif filt['type'] == "pipe":
            pass
        else:
            raise AssetException("Type %s not understood." % filt['type'])

        mime = config.ASSET_EXTS.get(fname.split(".")[-1], None)
    return (fname, text, clas)


def process_file(fname):
    # get asset directory
    source = None
    for asource in config.ASSET_SOURCES:
        # TODO: This is very bad
        if fname.find(asource['in']) == 0:
            source = asource
            break

    if source:
        # Read file
        try:
            f = open(fname)
        except FileNotFoundError:
            raise AssetException("File %s not found" % fname)
        text = f.read()
        f.close()

        # Process
        (fname, text, clas) = process(fname, text)

        # rename directory
        # TODO: This is very bad
        fname = fname.replace(source['in'], source['out'])

        # Write file
        make_sure_path_exists(fname)
        f = open(fname, "w")
        f.write(text)
        f.close()

        return (fname, text, clas)
    else:
        raise AssetException("File %s not in input sources" % fname)
