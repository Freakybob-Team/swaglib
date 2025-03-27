import swaglib

file_exists = swaglib.fileExists("files/swag.txt")

print('file exists') if file_exists else print("file doesn't exist")