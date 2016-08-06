'''
Created on Jul 29, 2016

@author: agruzman
'''
import yaml
import Utils.FileDictListUtils
import os
import sys
class all_configs():
    def _ensure_valid_categories(self):
        '''
        This function reads categories.yaml and makes sure the config files are correct
        1. <category>(scope) -
        2. categories are only known - specHDL, execHDL, verdictModel, etc
        '''
        pass
    def _read_yaml_configs(self,**kwargs):
        import re
        config_files_list=kwargs['list_of_cfgs']
        scp=kwargs['scope']
        for _ymlf in config_files_list: ##need to read them all, because it may be more than one config
            if os.path.isfile(_ymlf):
                f=open(_ymlf)
                try:
                    self.cfg=yaml.load(f) ## load the setup file
                except yaml.YAMLError as e:
                    print ("Error ({}) while reading a setup file ({})".format(str(e),_ymlf))
                    sys.exit('the setup file has syntax issues')
                categ_pattern=re.compile('\S+\((\S+)\)')
                for _category in self.cfg:
                    match = re.search(categ_pattern,_category)
                    if match:
                        print ("SCOPE=={}".format(match.group(1)))
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
            if _top_yaml == os.environ.get('TOPSCOPE'): ##Start from the top
                for _item in setup_obj.get_read_setup()[_top_yaml]:
                    self.topconfig.append(Utils.FileDictListUtils.ffordir(
                                                                                     what='file',
                                                                                     item=_item,
                                                                                     where=_where
                                                                                     )
                                          )
        self._read_yaml_configs(
                                list_of_cfgs=self.topconfig,
                                scope=os.environ.get('TOPSCOPE')
                                )
        print (self.cfg)
        #now it the right time to read them into dict of yaml

    pass