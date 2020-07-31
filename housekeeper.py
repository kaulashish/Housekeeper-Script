import os
from datetime import datetime
import time
import shutil

#Inputs to be given by user

directory = '/home/hadoop/PycharmProjects/Housekeeping-Script--master/Files' 	#input local files directory here
archive = '/home/hadoop/PycharmProjects/Housekeeping-Script--master/Archive'	#enter local archive location
hadoop_dir = '/usr/local/hadoop/bin/hdfs'  #can be retrieved by entering 'which hadoop' in terminal

#generating current date and datetime
today = datetime.today()

#moving files from 'directory' that are 3 days old to an archive
flag = 1
while(flag == 1): 
    try:
        file_list = os.listdir(directory)  #similar to pwd
        flag = 0
        for i in file_list:
            file = i
            file_dir = directory + '/' + file
            file_date = time.ctime(os.path.getmtime(file_dir)) #returns modified date and time of file
            file_date = datetime.strptime(file_date,'%c')
            time_diff = today-file_date
            if time_diff.days > 3:
                shutil.move(file_dir, archive)
                print('File "{}" moved to archive. [{} days old]'.format(file, time_diff.days))
        print('Archive location: {}'.format(archive))
    except FileNotFoundError:
        print('Invalid Directory.')

#storing the files from archive to hdfs within directory - tmp-Archive
os.system('start-all.sh') #starts all hadoop daemons
if os.system('{} dfs -test -e /user/hadoop/tmp-archive'.format(hadoop_dir)) == 0:
    print('Archive location exists...using current archive.')
else:
    os.system('{} dfs -mkdir /user/hadoop/tmp-archive'.format(hadoop_dir))
    print('Archive created -> /user/hadoop/tmp-archive')
archive_file_list = os.listdir(archive)
for j in archive_file_list:								#checks files within archive and stores it in hdfs
    archive_file_dir = archive + '/' + j
    os.system('{} dfs -put {} /user/hadoop/tmp-archive'.format(hadoop_dir, archive_file_dir)) 
print('Files added to HDFS in dir : /user/hadoop/tmp-archive')

