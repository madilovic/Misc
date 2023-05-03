# A function which splits SDF structural files
# This is applicable when a single SDF file contains multiple structures
# This script searches for sdf structures within the same folder
# Outputs the split structures into the new folder "split SDFs"
# (requires making one)

import os

for file in os.listdir():
    if file.endswith('.sdf'):
        sdf = open(file)
        compound = file.split(' ')[0]
        
        current_structure = ''
        current_id = None
        next_line = False
        
        
        
        for line in sdf:
            # record structuer id to be used for file output name
            if next_line:
                current_id = line.rstrip()
                next_line = False
            # detect a line for which a following line will be id
            if line.rstrip() == '> <chembl_id>':
                next_line = True
            # check for end of structure; if not - copy it for the current structure
            if line.rstrip() != '$$$$':
                current_structure += line
            # if end of structure ('$$$$'), save the current structure...
            else:
                current_structure += line
                output_file_name = './split SDFs/'+compound+' '+current_id+'.sdf'
                output = open(output_file_name,'w')
                output.write(current_structure)
                output.close()
                current_structure = ''
        sdf.close()
