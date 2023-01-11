# NotesScripting
Will try to create some python scripts that will automatically be ran on certains times during days I have classes, where markdown files will be created for every class and uploaded to my s3 bucket where I can view the notes on my personal website


## How they work
We have 3 files

> main.py </br>
> upload.py </br>
> aws.py </br>

**main.py**
This file is responsible for creating multiple .md files within a specificed directory where the .md files will be based on a dict/file and will contain headers for each.

**upload.py**
This script is responsible for turning the created .md files from main.py to html/ pdf files

**aws.py**
This file is responsible for the implementation of boto3 and to upload the contents for all the html files into the s3 bucket.


### Some functionalities:

- script runs when i have my laptop open during my first class of the day (taskscheduler to run `scriptA.py` and `scriptB.py` at different times based on schedule)
- Create a new directory on bishal/notes/*todays date*
  - number of files should be the number of classes I have for the day (classes are hardcoded and stored as a dictionary since there's only 4-5 classes)
    - name of the files should be data+class.md ex. Jan26CSE3380.md
- I write notes throughout my classes on markdown
- files will be converted to pdf or html
- after the last class the files will be uploaded to my s3 bucket using boto3

I'm currently working on s3 to find a way to import pages to my personal website
   
