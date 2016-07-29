'''
Created on Jul 29, 2016

@author: agruzman
'''
import os
import sys
def FindFileOrDir (**kwargs):
    i=kwargs['item']
    sp=kwargs['where']
    found = False
    for _cand_dir in sp:
        if kwargs['what'] == 'file':
            if os.path.isfile(os.path.join(_cand_dir,i)):
                found=True
                break
        else:
            if os.path.isdir(os.path.join(_cand_dir,i)):
                found=True
                break
    if found: 
        return os.path.join(_cand_dir,i)
    else: 
        sys.exit("Cant find  ({}) @ ({sp} as ({})".format(i,sp,kwargs['what']))
        