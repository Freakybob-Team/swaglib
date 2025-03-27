import swaglib

string = 'hello!'
encoded_string = swaglib.encodeBase64(string) 
decoded_string = swaglib.decodeBase64(encoded_string)

print(decoded_string)