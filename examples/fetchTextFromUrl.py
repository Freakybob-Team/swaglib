import swaglib

# a way to use fetchTextFromUrl

urlText = swaglib.fetchTextFromUrl('https://raw.githubusercontent.com/Nomaakip/swaggame/refs/heads/main/version.txt')

print(urlText)

# another way to use it

text = "1.2"
StrippedUrlText = urlText.strip()

if text == StrippedUrlText:
    print('same text')
else:
    print('the text isnt the same')