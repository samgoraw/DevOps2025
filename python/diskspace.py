#sellutil
#disk usage statistics
import shutil

total,used,free = shutil.disk_usage('/')

print(f"Total:{total//(2**30)} GB") #converting menory into GB
print(f"Used:{used//(2**30)} GB") #converting menory into GB
print(f"Free:{free//(2**30)} GB") #converting menory into GB

percentage_used = (used/total) *100
print(f"Disk Usage: {percentage_used:.2f}%") 
