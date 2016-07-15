'''
Created on Jul 10, 2016

@author: agruzman
'''
import yaml
import os
class setup:
    setupfile=str()
    scopes=dict() # dict of scope->subscopes relationship
    scopes_flat=list() #flat list of scopes
    sp=dict() 
    '''  This dictionary is tricky
        it has a full search path /sc/subscope1/subscope2 -(list of search pat
    '''
    
    
    def _init (self):
        ##READ setup file specified by ENV variable
        #populate the setup object with the data located in the setup file
        self.setupfile=os.environ.get('YSETUP') ##may be get a cmd line option
        
        pass
    def get_all_scopes_flat(self):
        pass ## returns list
    def get_scopes_structure(self):
        pass ##returns a dict
    def get_sp_by_scope (self, scope=os.environ.get(topscope=str())):
        pass ## scope has to be fully qualified
    def get_all_instances_of_scope(self,currentscope):
        pass ## This list in ideal case will have the length of 1, if more need to debug
    
    
    
    
    
                    
    
def main():
    a=dict()
    #f=open("module.yaml")
    f=open("setup.yaml")
    
    a=yaml.load(f)
    #print (a['vlog_opts'])
    print (a)

if __name__ == '__main__':
    main()