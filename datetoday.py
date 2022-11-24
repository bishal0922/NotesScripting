from datetime import date

#gets the date and returns it as a string in form of Mon#
def get_date():
    # Nov24
    return date.today().strftime('%b%d')

def get_full_date():
    # November 25, 2019
    return date.today().strftime('%B %d, %Y')

def get_date_file_name():
    # ThuNov24
    return date.today().strftime('%a%b%d')
