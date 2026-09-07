import psutil

cup_usage= psutil.cpu_percent(interval=1)
print(cup_usage);


