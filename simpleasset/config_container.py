"""
SimpleAsset config singleton
"""

import json
import os


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = "%s/default_config.json" % (PROJECT_ROOT)


class ConfigContainer(object):
    'Singleton containing configuration'

    def __init__(self):
        self.config = {}
        self.configured = False

    def load(self, configfile=None):
        'Loads the configuration from either ASSETCONFIG env variable, or DEFUALT_CONFIG'

        if not configfile:
            configfile = os.getenv('ASSETCONFIG', DEFAULT_CONFIG)

        if self.configured is False:
            cfl = open(configfile)
            self.config = json.load(cfl)
            cfl.close()
            self.config['PROJECT_ROOT'] = PROJECT_ROOT
            self.configured = True
        else:
            raise Exception('Already Configured')

    def __getattr__(self, name):
        'Override getattr() so config.SOME_VALUE works transparently'

        if not self.configured:
            self.load()
        return self.config[name]

    #def __str__(self):
        #if not self.configured:
            #self.load()
        #return json.dumps(self.config, indent=4, sort_keys=True)
