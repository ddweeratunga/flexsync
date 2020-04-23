# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:51:47 2020

@author: ddwee
"""

org_ids = ['MDS', 'MDMS']
spd_configs = ['E','EE','EB','EEB','EEBB']
num_meters = [1,2,3,4]
  
#get org id 
while True: 
    org = input("Enter the sync file ORG: ").upper()
    if org in org_ids:
        break
    else:
        print("Enter valid ORG")
#get sdp config    
while True:
    sdp_config = input("Enter SDP configuration: ").upper()
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
#create file name
if org == 'MDS':            
    filename = "8000-{}-{}-M{}.xml".format(org, sdp_config, meters)
else:
    filename = "8001-{}-{}-M{}.xml".format(org, sdp_config, meters)                 
#load and file to edit
file_handle = open(filename)
read_file = file_handle.read()