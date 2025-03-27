import swaglib

# a way to use it (generates a random string and writes it to swag.txt)

random_string = swaglib.generateRandomString(10)

swaglib.writeToFile('files/swag.txt', random_string)

# another way to use it

print(random_string)