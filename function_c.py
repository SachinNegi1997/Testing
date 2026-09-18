import os           # import linux commands 
import datetime

def run(command):
 return os.system(command)

#run('df -h')       # function call with argument
#run('du -sh')


def show_date():
 return datetime.datetime.today()


time = show_date()

print(time)
