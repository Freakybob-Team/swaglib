import swaglib

if swaglib.checkWifi():
    print('Wifi is enabled')
else:
    print('Wifi is disabled.')