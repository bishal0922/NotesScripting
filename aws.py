import os
import boto3  # pip install boto3
import datetoday
# Let's use Amazon S3 - s3 access object
s3 = boto3.client("s3")
BUCKET_NAME = "mygeneratedhtmlnotes"

#download from the s3 server
print("Root Directory of this project: \n\t" + os.getcwd())
#s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

os.chdir('../../../bishal/notes')

dir = datetoday.get_date_file_name()


directory = os.chdir(dir)
print(os.getcwd())
# iterate over files in
# that directory
for filename in os.listdir(directory):
    if os.path.isfile(filename) and filename.endswith('.html'):
        print(filename)
        #s3.upload_file(filename, BUCKET_NAME, dir+'/'+filename)
        print("File" + filename +  "uploaded to S3")




#s3.upload_file('testfile.txt', BUCKET_NAME, 'TESTING/tesstfile.txt')

