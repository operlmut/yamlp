'''
Created on Jul 29, 2016

@author: agruzman
'''
import os
import sys
def ffordir (**kwargs):
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
        return os.path.abspath(os.path.join(_cand_dir,i))##on windows it is \\file :(
        
    else: 
        sys.exit("Cant find  ({}) @ ({} as ({})".format(i,sp,kwargs['what']))
        