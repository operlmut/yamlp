'''
Created on Jul 29, 2016

@author: agruzman
'''
import yaml
import MakeConfig.Utils.FileDictListUtils
import os
import sys
class all_configs():
    def _read_yaml_configs(self):
        for _ymlf in self.topconfig:
            if os.path.isfile(_ymlf):
                f=open(_ymlf)
                try:
                    self.cfg=yaml.load(f) ## load the setup file
                except yaml.YAMLError as e:
                    print ("Error ({}) while reading a setup file ({})".format(str(e),_ymlf))
                    sys.exit('the setup file has syntax issues')
                f.close()
            else:
                print ('cant open file {}'.format(_ymlf))
                sys.exit('cant open the setup file')
        pass
    def read_yaml_configs(self):
        pass
    def __init__(self, setup_obj):
        self.topconfig=list()
        _where=setup_obj.get_sp_by_scope()
        #finding all of the yamls that are mentioned for configuration
        for _top_yaml in setup_obj.get_read_setup():
            if _top_yaml == os.environ.get('TOPSCOPE'):
                for _item in setup_obj.get_read_setup()[_top_yaml]:
                    self.topconfig.append(MakeConfig.Utils.FileDictListUtils.ffordir(
                                                                                     what='file',
                                                                                     item=_item,
                                                                                     where=_where
                                                                                     )
                                          )
        self.read_yaml_configs()
        #now it the right time to read them into dict of yaml

    pass