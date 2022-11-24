import os
import datetoday

#this part may need some changes depending upon where this .py file is located
# print(os.getcwd()) -> will get the current working directory where this file is located
os.chdir('../../../bishal/notes')
# print(os.getcwd()) -> will now go to the notes directory
print(os.getcwd())

# #read class_list.txt and store it in a list
# if os.path.exists('class_list.txt'):
#     with open('class_list.txt') as f:
#         class_list = f.readlines()
#         # strip the newline character '\n' from each line
#         class_list = [x.strip() for x in class_list]

# we should rather create file as a map
class_list = {
    'CSE3315': 'Theory of Computation',
    'COMS2302': 'Business Communication',
    'CSE3310': 'Intro to Software Engineering',
}


folder_name = datetoday.get_date_file_name()

#if there isn't the directory we want then 
dir = os.path.join(folder_name)

if not os.path.isdir(dir):
    os.mkdir(dir)
    os.chdir(dir)

    #gets Nov24
    month_day = datetoday.get_date()

    #read class_list.txt and append it to month_day
    for my_class in class_list:
        new_file_name = my_class + '_' + (month_day) + '.md'
        fp = open(new_file_name, 'w')
        
        #write the header
        fp.write('# '+ my_class + ' - ' +class_list.get(my_class) +'\n'+
            '### '+ datetoday.get_full_date() + '\n')    

else:
    print("The directory already exists")


#if the directory doesn't exits then create the directory called notes uploader
