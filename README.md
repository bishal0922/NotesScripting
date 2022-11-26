# NotesScripting
Will try to create some python scripts that will automatically be ran on certains times during days I have classes, where markdown files will be created for every class and uploaded to my s3 bucket where I can view the notes on my personal website


### Some functionalities:

- script runs when i have my laptop open during my first class of the day (taskscheduler to run `scriptA.py` and `scriptB.py` at different times based on schedule)
- Create a new directory on bishal/notes/auto 
  - number of files should be the number of classes I have for the day (classes are hardcoded and stored as a dictionary since there's only 4-5 classes)
    - name of the files should be data+class.md ex. Jan26CSE3380.md
- files will be converted to pdf or html
- after the last class the files will be uploaded to my s3 bucket using boto3
   
