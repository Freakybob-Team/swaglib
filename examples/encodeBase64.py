import swaglib

string = 'hello!'
encoded_string = swaglib.encodeBase64(string) 

print(encoded_string)