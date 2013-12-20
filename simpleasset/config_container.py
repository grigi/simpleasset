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

    def load(self):
        'Loads the configuration from either CAPI_CONFIG env variable, or DEFUALT_CONFIG'

        if self.configured is False:
            self.config = json.load(open(os.getenv('ASSETCONFIG', DEFAULT_CONFIG)))
            self.config['PROJECT_ROOT'] = PROJECT_ROOT
            self.configured = True
        else:
            raise Exception('Already Configured')

    def __getattr__(self, name):
        'Override getattr() so config.SOME_VALUE works transparently'

        if not self.configured:
            self.load()
        return self.config[name]
