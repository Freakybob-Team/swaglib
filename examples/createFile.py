import swaglib

# a way to use it
swaglib.createFile('swag', 'txt')

# another way to use it
print('Enter file number: ', end='')
file_number = int(input())

for i in range(1, file_number + 1):
    swaglib.createFile(f'swag{i}', 'txt')