#!usr/bin/python3

"""
This script is responsible for turning the created .md files from main.py to html/ pdf files
"""

import os
import date_formatter

# To turn .md to .html ==
# python3 -m markdown COMS2302_Nov24.md > COMS2302_Nov24.html
# To run .md to pdf ===
# os.system('mdpdf '+ file)

# assign directory back to our notes folder where the .md files were created
os.chdir('../../../bishal/notes')

#ThuNov25
directory = os.chdir(date_formatter.get_date_file_name())

#current working directory
print(os.getcwd())

# iterate over files in that direcotry
for filename in os.listdir(directory):
    if os.path.isfile(filename):
        #turning the markdown file into html
        os.system('python3 -m markdown ' + filename + ' > ' + filename[:-2] + 'html')

#changing directory to our project folder
#os.chdir('../../../projects/NotesScripting/NotesScripting')
