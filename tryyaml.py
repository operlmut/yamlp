'''
{
    'scopes': ['scope1', 'scope2', 'test_top_scope'], 
    'reserved': None, 
    'scopes_relations': [
                        {'test_top_scope': ['scope1']}, 
                        {'scope1': ['scope2']}, 
                        {'test_top_scope': ['scope2']}
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

'''
'''
Created on Jul 10, 2016

@author: agruzman
'''
import yaml
import os
import logging
class setup:
    setupfile=str()
    scopes=dict() # dict of scope->subscopes relationship
    scopes_flat=list() #flat list of scopes
    sp=dict() 
    '''  This dictionary is tricky
        it has a full search path /sc/subscope1/subscope2 -(list of search pat
    '''
    def validate_setup(self):
        pass
    
    def _init (self):
        ##READ setup file specified by ENV variable
        #populate the setup object with the data located in the setup file
        self.setupfile=os.environ.get('YSETUP') ##may be get a cmd line option
        f=open(self.setupfile)
        try:
            self.ymlsetup=yaml.load(f) ## load the setup file
        except yaml.YAMLError as e:
            print ("Error ({}) while reading a setup file ({})".format(str(e),self.setupfile) )
        self.validate_setup()

        
        pass
    def get_all_scopes_flat(self):
        pass ## returns list
    def get_scopes_structure(self):
        pass ##returns a dict
    def get_sp_by_scope (self, scope=os.environ.get('TOPSCOPE')):
        pass ## scope has to be fully qualified
    def get_all_instances_of_scope(self,currentscope):
        pass ## This list in ideal case will have the length of 1, if more need to debug
    
    
    
    
    
                    
def main():
    read_and_print()
    #setup=setup();
def read_and_print():
    
    a=dict()
    #f=open("module.yaml")
    f=open("setup.yaml")
    
    a=yaml.load(f)
    #print (a['vlog_opts'])
    print (a)

if __name__ == '__main__':
    main()