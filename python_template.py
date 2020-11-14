"""
This script contains a template for designing python scripts with software engineering best practicesin mind, and ample comments to understand why.  

Material adapted PEP8 and from Real Python: 
https://realpython.com/python-main-function/
"""

#Define global variables at the top of the page, just under module docstrings.
#Use all caps to distinguish them as global scope
GLOBAL_VARIABLE = 'foo'

"""
Import libraries next, on separate lines for each module.
ordered as such:
    1) standard libraries
    2) third-party libraries
    3) local modules or partial library imports

Below, we demonstrate some imports. Note that the script only uses the functions imported from 'csv' module. It is poor practice to leave unused import statements in scripts.
"""
#A standard library
import os
#A third party library
import pandas as pd
#A local import
import local_module as lm
#Partial libary import (both functions can go on one line)
from csv import DictReader, writer

""" 
Define a main() function to hold the primary workflow for the script,
when executed from the command line. The are a few features to this design:
1) main() should only be a few lines long. Call other well-named functions as needed. This makes the overall workflow of the script very clear.
2) If the script is imported as a module, the logic in main() not run (see line XX). Any functions defined in the script can be reused. Now any python script can serve dual-roles as execuatble or module.
3) Low-level languages (C++, Java) often require a main() function as the 'entry point' for execution. Python reads line-by-line instead, executing commands as called or compiling functions when defined. This simulates the main() entry point function.
"""

def main():
    
    data = import_some_data(input_file)

    processed_data = process_some_data(data)
    
    export_some_data(processed_data,output_file)

    #<END OF PROGRAM>

"""
Define helper functions underneath the main function. Be sure to include docstrings describing
what each function does, the inputs that it expects, and the output format. You should limit
changes to variables to those only within the function's local scope. Global variable can be referenced, but avoid making changes to them.
"""
def import_some_data(input_file):
    """
    In this example, we take a csv file containing records of every pet registered in the city.
    We want to find how many pets each owner has and output the result as a csvfile.

    INPUT: a string containing the path to a csvfile
    OUTPUT: dict(key:OwnerID,value:list_of_pets)
    """
    data = {}
    with open(input_file,'r+') as f:

        #DictReader reads the csv as a dictionary with fieldnames as keys, 
        #allowing us to access fields by the header name rather than location
        #if a column is added or drops from the file, we still read the field
        #if the field name is changed in the file, we throw an error
        #this is better than reading the field by its location and allowing errors to pass through
        csv_file = DictReader(f,delimiter=',')
        
        for row in csv_file:

            #Parse row, declaring the expected type at import 
            #will also help to raise errors if things change 
            owner_id = int(row['OwnerID']
            pet_id = int(row['PetID'])
            
            #If the owner has not been added to our data dictionary,
            #initialize an empty list
            if owner_id not in data:
                data[owner_id] = []

            #Add the pet to the owners list of pets
            data[owner_id].append(pet_id)

    return data
            
def process_some_data(data):
    """
    A second helper function. Calculates the average of each column in the csvfile.

    INPUT: dict(key:OwnerID,value:list_of_pets)
    OUTPUT: dict(keys:OwnerID,value:number_of_pets)
    """
    
    #Use dict.items() method to iterate through dictionary
    #unpacking both key and value
    for owner_id, list_of_pets in data.items():

        #Overwrite the list_of_pets with number_of_pets
        data[owner_id] = len(list_of_pets)
    
    return data

def export_some_data(processed_data,output_file):
    """
    A third helper function.

    INPUTS: 
        processed_data: dict(key:OwnerID,value:number_of_pets) 
        output_file: a string defining the output file path.
    OUTPUT: None, writes a csvfile. One row for every owner.
    """

    with open(output_file,'w') as csv_file:
        report_writer = writer(csv_file,delimiter=',')
        report_writer.writerow(['OwnerID','Number of pets'])
        for owner_id, num_pets in processed_data.items():
            report_writer.writerow([owner_id, num_pets])
            return
    
# The logic defining the dual role of files a scripts or as modules is shown below
# If the script is executed from command line (or %run in notebook), 
# __name__ is initialized as '__main__'
# If the script is imported as a module,
# __name__ is initialized with the same name as the module (python_template in this case)
if '__name__' == '__main__':
    main()
