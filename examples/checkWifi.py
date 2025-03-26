import swaglib

# 1st way to use it
wifi_status = swaglib.checkWifi()

if wifi_status:
    print('Wifi is enabled.')
else:
    print('Wifi is disabled.')

# 2nd way to use it

if swaglib.checkWifi():
    print('Wifi is enabled.')
else:
    print('Wifi is disabled.')

# 3rd way to use it 

print(swaglib.checkWifi())

# these arent the only ways to use it, these are only examples.