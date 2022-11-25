import os
import datetoday
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# command is : python3 -m markdown COMS2302_Nov24.md > COMS2302_Nov24.html

# assign directory
os.chdir('../../../bishal/notes')

dir = datetoday.get_date_file_name()
directory = os.chdir(dir)
print(os.getcwd())
# iterate over files in
# that directory
for filename in os.listdir(directory):
    if os.path.isfile(filename):
        file = filename
        #turning the markdown file into html
        os.system('mdpdf '+ file)
        #os.system('python3 -m markdown ' + file + ' > ' + file[:-2] + 'html')


# Use a service account.
#print working directory
# Users/bishal/Documents/bishal/notes/ThuNov24

#changing directory to our project folder
os.chdir('../../../projects/NotesScripting/NotesScripting')


# cred = credentials.Certificate('mynotes-cede7-firebase-adminsdk-nxksw-f19f4e0b57.json')

# app = firebase_admin.initialize_app(cred)

# db = firestore.client()
# now we have all the files in html format and we can upload them to the amazon s3 server

# add a file to the database
