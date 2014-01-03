"Simple Asset pipeline toolset"

VERSION = '0.0.1'

import simpleasset.config_container

# Initialise config singleton
config = simpleasset.config_container.ConfigContainer() # pylint: disable=C0103

class AssetException(Exception):
    "Standard Asset exception"
    pass

from simpleasset.match import process, process_file
