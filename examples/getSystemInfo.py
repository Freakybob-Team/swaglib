import swaglib

# a way to use it

system_info = swaglib.getSystemInfo()

info = ['os', 'architecture', 'ip_address']

for i in info:
    print(f"{i.capitalize()}: {system_info[i]}")

# another way to use it

print(system_info['os'])