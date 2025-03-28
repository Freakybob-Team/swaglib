import os
import requests
import subprocess
import json
import base64
import random
import hashlib
import platform
import socket
import datetime
import string

version = "0.2.1"

def greet(name):
    print(f"hello {name}!!")

def classic_greet(name):
    print(f"Hello, {name}!")

def fetchTextFromUrl(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None  

def getResponseStatusFromUrl(url: str) -> int:
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")

def playAudio(file_path: str) -> None:
    subprocess.run(["ffplay", "-nodisp", "-autoexit", file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def checkWifi():
    try:
        requests.get("https://google.com", timeout=2)
        return True
    except requests.exceptions.RequestException:
        return False 

def writeToFile(path, content):
    mode = 'a' if os.path.exists(path) else 'w'
    with open(path, mode) as file:
        file.write(content)

def createFile(file_name, file_extension):
    file_path = f"{file_name}.{file_extension}"
    with open(file_path, 'w') as file:
        pass
    return file_path

def removeFile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def writeBytes(file_path, bytes_number, text):
    txt_string = (text * (bytes_number // len(text) + 1))[:bytes_number]
    mode = 'w' if not os.path.exists(file_path) else 'a'
    with open(file_path, mode) as file:
        file.write(txt_string)

def getSystemInfo():
    return {
        'os': platform.system(),
        'os_release': platform.release(),
        'machine': platform.machine(),
        'architecture': platform.architecture(),
        'processor': platform.processor(),
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname())
    }

def generateRandomString(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def encodeBase64(text):
    return base64.b64encode(text.encode()).decode()

def decodeBase64(encoded_text):
    return base64.b64decode(encoded_text).decode()

def hashString(text, algorithm='sha256'):
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).hexdigest()

def saveJson(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def loadJson(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def getCurrentTimestamp():
    return datetime.datetime.now().isoformat()

def pingHost(host, count=4):
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, str(count), host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False
    
def getFileSize(file_path):
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    return None

def listFiles(directory):
    return os.listdir(directory)

def readFile(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except IOError as e:
        print(f"Error reading {file_path}: {e}")
    return None

def downloadFile(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

def fileExists(file_path):
    return os.path.exists(file_path)

def shellRun(command):
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout
