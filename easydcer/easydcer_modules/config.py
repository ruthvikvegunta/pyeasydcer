import json
from collections import OrderedDict
from datetime import datetime
import time
import os

class checkConfig():
    def __init__(self, file_name, mode = ''):
        self.file_name = file_name
        self.mode = mode
        
    def getInfo(self):
        if self.mode == 'force_change':
            return self.forceConfigChange()
        else:    
            try:
                with open(self.file_name) as file_read_object:
                    pydcer_saved_config = json.load(file_read_object)
                    current_time = datetime.now()
                    config_saved_time = datetime.strptime(pydcer_saved_config['time_stamp'], '%c')
                    difference_in_time = (current_time - config_saved_time).seconds
                    if(difference_in_time >= 3600):
                        return self.forceConfigChange()
                    else:
                        return pydcer_saved_config
            except FileNotFoundError:
                return self.forceConfigChange()

    def forceConfigChange(self):
        subscription_name = input('\nPlease enter the subscription name:  ')
        default_path = input('\nPlease enter the path for the default directory where you have all your clones:  ')
        if os.name == 'posix':
            path = os.sep
            for item in default_path.split(os.sep):
                if item != '':
                    path += item + os.sep
        elif os.name == 'nt':
            path = os.sep
            for item in default_path.split(os.sep):
                if item != '':
                    path += item + os.sep
        pydcer_saved_config = OrderedDict()
        pydcer_saved_config['subscription'] = subscription_name
        pydcer_saved_config['path'] = path
        pydcer_saved_config['time_stamp'] = (datetime.now()).strftime('%c')

        pydcer_config_json = json.dumps(pydcer_saved_config)

        with open(self.file_name , 'w') as file_write_object:
            file_write_object.write(pydcer_config_json)
        return pydcer_saved_config
