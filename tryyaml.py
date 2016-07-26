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
import re
class setup:
    setupfile=str()
    scopes=dict() # dict of scope->subscopes relationship
    scopes_flat=list() #flat list of scopes
    _scopes_hierarchies=list()
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
        _extracted_scope_name=re.sub('.*\/','', scope)
        for subscope in self.scopes[_extracted_scope_name]:
            _tmp_el=scope+"/"+subscope
            l.append(_tmp_el)
            if subscope in self.scopes:
                self._make_scopes_hierarchy(l, _tmp_el)
        return l
    def _make_sp_by_scope(self):
        #update SP according to the scopes definitions
        tmp_sp_dict=dict()
        for _spscope in self.sp:
            if _spscope in self._scopes_hierarchies: 
                #print ('SP for ({}) has been found ({})'.format(_spscope,self.sp[_spscope]))
                tmp_sp_dict[_spscope]=self.sp[_spscope]
                pass
            else :
                sscope_pattern=re.compile(_spscope)
                for _potential_sscope_withno_sp in self._scopes_hierarchies:
                    match=re.search(sscope_pattern,_potential_sscope_withno_sp)
                    if _potential_sscope_withno_sp not in self.sp and match :
                        tmp_sp_dict[_potential_sscope_withno_sp]=self.sp[_spscope]
        self.sp=tmp_sp_dict
        #now need to validate of all scopes are ok with their SP
        missing_sp=list()
        for scope in self._scopes_hierarchies:
            if scope not in self.sp:
                missing_sp.append(scope)
        if len(missing_sp) > 0 :
            for missing in missing_sp:
                print('Error, SP was not properly defined for ({})'.format(missing))
            sys.exit('Missing SP definition')    
        pass
        
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
        for D in self.ymlsetup['sp']:
            self.sp.update(D)
        self._scopes_hierarchies=self._make_scopes_hierarchy([self.get_top_scope()],self.get_top_scope())
        self.sp=self._make_sp_by_scope() ##corrected values of sp
        pass
    def get_read_setup(self):
        return self.ymlsetup['read_setup'] ## need files locations to be fully resolved 
        
    def get_all_scopes_flat(self):
        if os.environ.get('TOPSCOPE') not in self.ymlsetup['scopes']:
            print ("Error, the top scope defined by setup is ({}) not found in the scopes collection {}".format(os.environ.get('TOPSCOPE'), self.ymlsetup['scopes']))
            sys.exit("Error found, in setup process...Exiting")
        else:
            return self.ymlsetup['scopes']
        pass ## returns list
    def get_scopes_structure(self):
        return self._scopes_hierarchies #returns a list of scopes in the format of top/sub1/sub2...
    def get_sp_by_scope (self, scope=os.environ.get('TOPSCOPE')):
        pass ## scope has to be fully qualified
    def get_all_instances_of_scope(self,currentscope): #returns list
        scope_pattern =re.compile(currentscope)
        l=list()
        found=False
        for sc in self._scopes_hierarchies:
            match = re.search(scope_pattern,sc)
            if match  and (currentscope in self.get_all_scopes_flat()):
                l.append(sc)
                found=True
        if not found : sys.exit('Can not find scope ({}) specified'.format(currentscope))
        return l
    
    
    
    
                    
def main():
    #read_and_print()
    mainsetup=setup() ##instance of the first setup object
    #print (mainsetup.get_all_scopes_flat())
    #print (mainsetup.get_all_instances_of_scope('scope2'))
    for sc in mainsetup.get_scopes_structure():
        print (sc)
    print (mainsetup.get_read_setup())
def read_and_print():
    
    a=dict()
    #f=open("module.yaml")
    f=open("setup.yaml")
    
    a=yaml.load(f)
    #print (a['vlog_opts'])
    print (a)

if __name__ == '__main__':
    main()