import swaglib

jsonData = {
    "name": "swaglib",
    "version": swaglib.version
}

swaglib.saveJson(jsonData, "files/json/swaglib.json")