# Housekeeper-Script

OBJECTIVES:
A python script used to automate managing your files older than 3 days in your local file system into an archive as well as HDFS directory. 

SUMMARY:
This is my first project for python that uses various modules such as OS, datetime, shutil and time in order to manage the files in the directory which is given by
user input in the python file attached in the repo. Other requirements include providing the Hadoop path which can be retrieved by entering 'which hadoop' in a terminal.
The files in the main directory is scanned to retrieve the date which if more than 3 days will move those respective files into an archive and transfer them into hdfs.

STEPS TO RUN:
1) Open the python file and provide all the inputs for the variables 'directory', 'archive' and 'hadoop_path'
2) In order to schedule the file to run everyday, you can use Cron by entering 'crontab -e' in the terminal and pasting the following code at the end of file with respective changes for the directory for it (in this case, script will run everyday at 5PM or 1700 hours) -->


`00 17 * * * python path/to/file > /path/to/log date +\%d\%m\%Y\%H\%M-cron.log 2>&1` ( `date +\%d\%m\%Y\%H\%M` is within grave accent ' ` ' )

