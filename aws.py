#!usr/bin/python3

"""
This file is responsible for the implementation of boto3 and to upload the contents for all the html files into the s3 bucket.
"""

import os
import boto3
import date_formatter
from bs4 import BeautifulSoup

#s3 accessing object using boto
s3 = boto3.client("s3")
BUCKET_NAME = "mygeneratedhtmlnotes"

#download from the s3 server
print("Root Directory of this project: \n\t" + os.getcwd())
#s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

#now we change directory to out notes folder
os.chdir('../../../bishal/notes')

# ex.ThuNov25
directory_formatted = date_formatter.get_date_file_name()
directory = os.chdir(directory_formatted)

print(os.getcwd())

# iterate over files in that directory
for filename in os.listdir(directory):
    #if its a file and it ends with .html (type is html)
    if os.path.isfile(filename) and filename.endswith('.html'):

        #reading the file with beautiful soup
        HTMLFile = open(filename, "r")
        index = HTMLFile.read()

        #our contents of the html file are being passed on as Body
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=index,  ContentType='text/html')

        print("File (" + filename +  ") uploaded to S3")



