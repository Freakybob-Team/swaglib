import requests
import subprocess

def greet(name):
    print(f"hello {name}!!")

def fetchTextFromUrl(url: str) -> str:
    response = requests.get(url)

    print(response.text)

def getResponseStatusFromUrl(url: str) -> str:
    response = requests.get(url)
    print(response.status_code)

def playAudio(file_path: str) -> str:
    subprocess.run(["ffplay", "-nodisp", "-autoexit", file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def checkWifi():
    try:
        requests.get("https://google.com", timeout=2)
        return True
    except requests.exceptions.RequestException:
        return False 
