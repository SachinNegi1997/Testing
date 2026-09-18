import datetime
import shutil    #inbuilt module specifically focusing on copying, moving, renaming taking two arguments (src,dest)
import os


def backup_file(source,destination):

 today = datetime.date.today()                                 
 backup_file_name=os.path.join(destination,f"backup_myvenv{today}")  # os.path.join (combine multiple component of path ) destination of backupfile with date 
 shutil.make_archive(backup_file_name,'gztar',source) # gunzip file , compress file 

source ="/home/sachin/myvenv"
destination="/home/sachin/backup"

backup_file(source,destination)  #function call 
