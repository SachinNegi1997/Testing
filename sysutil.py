import psutil
import os




def extra(fun):

 def wrapper():
   print (os.system('df -h'))
   print (os.system('uptime'))
   print (os.system('du -sh'))
   print (os.system('free -h'))
   fun()
 return wrapper

@extra
def all_detail():

  cpu = psutil.cpu_percent(interval=1)
  memory = psutil.virtual_memory().percent
  usage= psutil.disk_usage("/").percent

  system_info={

                "cpu" : cpu,
                "memory" : memory,
                "usage" : usage
                }
               
  #return system_info
all_detail()

  


