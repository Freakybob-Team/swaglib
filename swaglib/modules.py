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

version = "0.2.0"

def greet(name):
    print(f"hello {name}!!")

def classic_greet(name):
    print(f"Hello, {name}!")

def fetchTextFromUrl(url: str) -> str:
    response = requests.get(url)
    return response.text

def getResponseStatusFromUrl(url: str) -> int:
    response = requests.get(url)
    return response.status_code

def playAudio(file_path: str) -> None:
    subprocess.run(["ffplay", "-nodisp", "-autoexit", file_path], 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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

def removeFile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def writeBytes(file_path, bytes_number, text):
    txt_string = (text * (bytes_number // len(text) + 1))[:bytes_number]
    mode = 'w' if not os.path.exists(file_path) else 'a'
    with open(file_path, mode) as file:
        file.write(txt_string)

def get_system_info():
    return {
        'os': platform.system(),
        'os_release': platform.release(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname())
    }

def generate_random_string(length=10):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(encoded_text):
    return base64.b64decode(encoded_text).decode()

def hash_string(text, algorithm='sha256'):
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).hexdigest()

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_current_timestamp():
    return datetime.datetime.now().isoformat()

def ping_host(host, count=4):
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

def readFile(file):
    if os.path.exists(file):
        with open(file, 'r'):
            return file.read()
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

def getSysInfo():
    return {
        "OS": platform.system(),
        "Version": platform.version(),
        "Architecture": platform.architecture()
    }

def classic_greet(name):
    print(f"Hello, {name}!")
