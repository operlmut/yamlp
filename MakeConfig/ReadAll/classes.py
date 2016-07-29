'''
Created on Jul 29, 2016

@author: agruzman
'''
import yaml
import MakeConfig.Utils.FileDictListUtils
import os
class all_configs():
    def __init__(self, setup_obj):
        self.topconfig=list()
        _where=setup_obj.get_sp_by_scope()
        for _top_yaml in setup_obj.get_read_setup():
            if _top_yaml == os.environ.get('TOPSCOPE'):
                for _item in setup_obj.get_read_setup()[_top_yaml]:
                    self.topconfig.append(MakeConfig.Utils.FileDictListUtils.ffordir(
                                                                                     what='file',
                                                                                     item=_item,
                                                                                     where=_where
                                                                                     )
                                          )
    pass