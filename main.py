#!/usr/bin/python3

"""
This file is responsible for creating multiple .md files within a specificed directory
The .md files will be based on a dict/file and will contain headers for each
"""

import os
import date_formatter
import logging

logger = logging.getLogger(__name__)  

# changing our os working directory to our destination notes folder
os.chdir('../../../bishal/notes')

# print(os.getcwd()) -> will now go to the notes directory
logging.debug("The directory where we have this notes folder is: \n\t" + os.getcwd())

# we should rather create file as a map
class_list = {
    "CSE 3380": "Linear Algebra",
    "CSE 3302": "Programming Languages",
    "CSE 3320": "Operating Systems",
}


#folder_name is the formatted date ex. ThuNov25
folder_name_formmated = date_formatter.get_date_file_name()

#if there isn't the directory we want then 
#our directory path
dir = os.path.join(folder_name_formmated)
logging.debug("directory we create from line 25" + dir)


if not os.path.isdir(dir):
    #if the directory doesn't exist then we make and enter into it
    os.mkdir(dir)
    os.chdir(dir)

    #gets Nov24 as a string
    month_day_formatted = date_formatter.get_date()

    #read class_list.txt (or a dict) and append it to month_day_formatted
    for my_class in class_list:
        new_file_name = my_class + '_' + (month_day_formatted) + '.md'
        fp = open(new_file_name, 'w')
        
        #write the header
        fp.write('# '+ my_class + ' - ' +class_list.get(my_class) +'\n'+
            '### '+ date_formatter.get_full_date() + '\n')    
else:
    print("The directory already exists")
