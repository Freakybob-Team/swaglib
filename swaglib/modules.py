import os
import requests
import subprocess

version = "0.1.9"

def greet(name):
    print(f"hello {name}!!")

def fetchTextFromUrl(url: str) -> str:
    response = requests.get(url)

    return response.text

def getResponseStatusFromUrl(url: str) -> str:
    response = requests.get(url)
    return response.status_code

def playAudio(file_path: str) -> str:
    subprocess.run(["ffplay", "-nodisp", "-autoexit", file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def checkWifi():
    try:
        requests.get("https://google.com", timeout=2)
        return True
    except requests.exceptions.RequestException:
        return False 

def writeToFile(path, content):
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write(content)
    else:
        with open(path, 'a') as file:
            file.write(content)

def createFile(file_name, file_extension):
    file = f"{file_name}.{file_extension}"
    with open(file, 'a') as file:
        return

def writeBytes(file_path, bytes_number, text):
    txt_string = (text * (bytes_number // len(text) + 1))[:bytes_number]

    mode = 'w' if not os.path.exists(file_path) else 'a'
    with open(file_path, mode) as file:
        file.write(txt_string)

def classic_greet(name):
    print(f"Hello, {name}!")
