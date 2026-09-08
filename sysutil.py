import psutil

def all_detail():

  cpu = psutil.cpu_percent(interval=1)
  memory = psutil.virtual_memory().percent
  usage= psutil.disk_usage("/").percent

  system_info={

                "cpu" : cpu,
                "memory" : memory,
                "usage" : usage
                }
               
  return system_info


  


