# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:51:47 2020

@author: ddwee
"""
sample_files = {'mds_e_1' : '8000-MDS-E.xml', 'mds_ee_1' :'8000-MDS-EE.xml','mds_eb_1' :'8000-MDS-EB.xml', 
                'mds_eeb_1' :'8000-MDS-EEB.xml', 'mds_eebb_1' :'8000-MDS-EEBB.xml', 'mdms_e_1' : '8000-MDMS-E.xml', 
                'mdms_ee_1' :'8000-MDMS-EE.xml'}


org_ids = ['mds', 'mdms']
spd_configs = ['e','ee','eb','eeb','eebb']
num_meters = [1,2,3,4]

def select_file():  
    # this fucntion return the flexSync file to be loaded from the sample file 
    
    #get org id 
    while True: 
        org = input("Enter the sync file ORG: ").lower()
        if org in org_ids:
            break
        else:
            print("Enter valid ORG")
    #get sdp config    
    while True:
        sdp_config = input("Enter SDP configuration: ").lower()
        if sdp_config in spd_configs:
            break
        else:
            print("Sample file not available for the selected sdp configuration")
    #get number of meters
    while True:
        meters = int(input("Number of meter's required: "))
        if meters in num_meters:
            break 
        else:
            print("Sample file not available for the selected number of meters")
   
    #file selection on user input                
    if org == 'mds' and sdp_config == 'e' and meters == 1:
        file = "{}{}{}".format(org, sdp_config, meters)
    elif org == 'mds' and sdp_config == 'ee' and meters == 1:
        file = 'mds_ee_1'
    elif org == 'mds' and sdp_config == 'eb' and meters == 1:
        file = 'mds_eb_1'
    elif org == 'mds' and sdp_config == 'eeb' and meters == 1:
        file = 'mds_eeb_1'
    elif org == 'mds' and sdp_config == 'eebb' and meters == 1:
        file = 'mds_eebb_1'
        
    elif org == 'mdms' and sdp_config == 'e' and meters == 1:
        file = 'mdms_e_1'
    elif org == 'mdms' and sdp_config == 'ee' and meters == 1:
        file = 'mdms_ee_1'
    elif org == 'mdms' and sdp_config == 'eb' and meters == 1:
        file = 'mdms_eb_1' 
    elif org == 'mdms' and sdp_config == 'eeb' and meters == 1:
        file = 'mdms_eeb_1' 
    elif org == 'mdms' and sdp_config == 'eebb' and meters == 1:
        file = 'mdms_eebb_1'             
    
 
    
        
    return(file)
    
    
     
    
    
    
print(select_file())
