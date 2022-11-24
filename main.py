import os
from datetime import date
#original directory default is /users/bishal 
#now we are in: /Users/bishal/Documents/bishal/notes

#this part may need some changes depending upon where this .py file is located
print(os.getcwd())
os.chdir('../../../bishal/notes')

#prints the current working directory
print(os.getcwd())

#if there isn't the directory we want then 
dir = os.path.join('today1')
if not os.path.isdir(dir):
    print("doesn't exist")
    #gets Nov24
    fstr = date.today().strftime('%b%d')
    
    print(fstr)
else:
    print("The directory already exists")


#if the directory doesn't exits then create the directory called notes uploader
