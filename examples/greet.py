import swaglib

swaglib.greet('g')

# 2nd way
swaglib.classic_greet('g')

# actual implementation

yourname = input()

swaglib.greet(yourname)
# or
swaglib.classic_greet(yourname)