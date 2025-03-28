import swaglib

diskInfo = swaglib.getDiskInfo()

print(diskInfo)

# only prints the free disk space
print(f'Free space: {diskInfo["free"]}')