'''
{
    'scopes': ['scope1', 'scope2', 'test_top_scope'], 
    'reserved': None, 
    'scopes_relations': [
                        {'test_top_scope': ['scope1','scope3']}, 0
                        {'scope1': ['scope2']},         1
    ], 
    'sp': [
        {'scope1': ['$HOME/workspace/sp1,$HOME/workspace/sp2', '$HOME/workspace/sp3']}, 
       {'scope2': ['$HOME/workspace//sp9,$HOME/workspace/sp1']}
    ], 
    'read_setup': [
        {'scope1': ['scope1s.yaml']}, 
        {'scope2': ['scope2s.yaml', 'onemore.yaml']}
    ]
}

''''''
from xml.etree.ElementTree import _Element_Py
 

@author: agruzman
'''
import yaml
import os
import logging
import  sys

class setup:
    setupfile=str()
    scopes=dict() # dict of scope->subscopes relationship
    scopes_flat=list() #flat list of scopes
    scopes_hierarchies=dict()
    sp=dict() 
    '''  This dictionary is tricky
        it has a full search path /sc/subscope1/subscope2 -(list of search pat
    '''
    @staticmethod
    def get_top_scope():
        if os.environ.get('TOPSCOPE') != None :
            return os.environ.get('TOPSCOPE')
        else :
            sys.exit('top scope is not defined')
    def validate_setup(self):
        print ("validating setup given by ({})".format(self.setupfile))
        pass
    def _make_scopes_hierarchy(self,l,scope): #list where hierarchies are stored
        import re
        _extracted_scope_name=re.sub('.*\/','', scope)
        for subscope in self.scopes[_extracted_scope_name]:
            _tmp_el=scope+"/"+subscope
            l.append(_tmp_el)
            if subscope in self.scopes:
                self._make_scopes_hierarchy(l, _tmp_el)
            print (_tmp_el)
        
        
        
    def __init__ (self):
        ##READ setup file specified by ENV variable
        #populate the setup object with the data located in the setup file
        self.setupfile=os.path.expandvars(os.environ.get('YSETUP')) ##may be get a cmd line option
        print("Trying to read the setup file ({})".format(self.setupfile))
        if os.path.isfile(self.setupfile):
            f=open(self.setupfile)
            try:
                self.ymlsetup=yaml.load(f) ## load the setup file
            except yaml.YAMLError as e:
                print ("Error ({}) while reading a setup file ({})".format(str(e),self.setupfile))
                sys.exit('the setup file has syntax issues')
            self.validate_setup()
        else:
            print ('cant open file {}'.format(self.setupfile))
            sys.exit('cant open the setup file')
        for D in self.ymlsetup['scopes_relations']:
            self.scopes.update(D)  
        self._make_scopes_hierarchy([],self.get_top_scope())     
                                
        pass
    
    def get_all_scopes_flat(self):
        if os.environ.get('TOPSCOPE') not in self.ymlsetup['scopes']:
            print ("Error, the top scope defined by setup is ({}) not found in the scopes collection {}".format(os.environ.get('TOPSCOPE'), self.ymlsetup['scopes']))
            sys.exit("Error found, in setup process...Exiting")
        else:
            return self.ymlsetup['scopes']
        pass ## returns list
    def get_scopes_structure(self):
        pass ##returns a dict
    def get_sp_by_scope (self, scope=os.environ.get('TOPSCOPE')):
        pass ## scope has to be fully qualified
    def get_all_instances_of_scope(self,currentscope):
        pass ## This list in ideal case will have the length of 1, if more need to debug
    
    
    
    
    
                    
def main():
    #read_and_print()
    mainsetup=setup() ##instance of the first setup object
    #print (mainsetup.get_all_scopes_flat())
    
def read_and_print():
    
    a=dict()
    #f=open("module.yaml")
    f=open("setup.yaml")
    
    a=yaml.load(f)
    #print (a['vlog_opts'])
    print (a)

if __name__ == '__main__':
    main()