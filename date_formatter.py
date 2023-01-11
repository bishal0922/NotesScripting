#The purpose of this file is for us to attain formatted Date Strings

from datetime import date

# Nov24
def get_date():
    return date.today().strftime('%b%d')

# November 25, 2019
def get_full_date():
    return date.today().strftime('%B %d, %Y')

# ThuNov24
def get_date_file_name():
    return date.today().strftime('%a%b%d')

