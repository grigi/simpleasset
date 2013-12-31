from simpleasset import config
from simpleasset import filters

ASSET_EXTS = {
    "tmpl":     "text/generictemplate",
    "template": "text/generictemplate",
    "jinja":    "text/jinja2"
}

ASSET_CLASSES = {
    "": [
        "text/generictemplate",
        "text/jinja2"
    ],
    "JS": [],
    "CSS": []
}

ASSET_FILTERS = {
    "text/generictemplate": {
        "type": "python",
        "func": "jinja2_filter"
    },
    "text/jinja2": {
        "type": "python",
        "func": "jinja2_filter"
    }
}

ASSET_SOURCES = [
    {
        "in": "samples",
        "out": "samples/out"
    }
]

ASSET_CONTEXT = {
    "name": "John Doe",
    "chain_name": "{{ name }}"
}

def process(fname, text, clas=""):
    mime = ASSET_EXTS.get(fname.split(".")[-1], None)
    while mime:
        filt = ASSET_FILTERS[mime]

        if filt['type'] == "python":
            try:
                fun = getattr(filters, filt['func'])
            except AttributeError:
                raise Exception("Filter %s not available." % filt['func'])
            text = fun(text, ASSET_CONTEXT)
            fname = ".".join(fname.split(".")[:-1])

        elif filt['type'] == "pipe":
            pass
        else:
            raise Exception("Type %s not understood." % filt['type'])

        mime = ASSET_EXTS.get(fname.split(".")[-1], None)
    return (fname, text, clas)

def process_file(fname):
    # Read file
    f = open(fname)
    text = f.read()
    f.close()

    # Process
    (fname, text, clas) = process(fname, text)

    # rename directory
    for source in ASSET_SOURCES:
        # TODO: This is very bad
        if fname.find(source['in']) == 0:
            fname = fname.replace(source['in'], source['out'])
            break
    
    # Write file
    
    return (fname, text, clas)
