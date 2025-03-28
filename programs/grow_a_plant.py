import swaglib as sl
import random as rd

print("grow a plant | 0.0.1")

file_path = "saveData/save.json"
default_stats = {"level": 0, "xp": 0, "required_xp": 10}

playerStats = sl.loadJson(file_path) if sl.fileExists(file_path) else default_stats

def water():
    global playerStats
    
    random_xp = rd.randint(1, 10 + playerStats["level"])
    playerStats["xp"] += random_xp
    
    if playerStats["xp"] > playerStats["required_xp"]:
        
        playerStats["level"] += 1
        print(f'you leveled up! you are now level {playerStats["level"]}.')
        
        playerStats["xp"] -= playerStats["required_xp"]
        playerStats["required_xp"] += 50
        
        sl.saveJson(playerStats, "saveData/save.json")
        
        return
        
    print(f'+{random_xp}.')
    
    sl.saveJson(playerStats, "saveData/save.json")
    
def exit_game():
    exit()
    

def game():
    
    options = {
        "1": water,
        "2": exit_game
    }
    
    print("1. water your plant\n2. exit")
    option = str(input())
    
    if option in options:
        options[option]()
        game()
    else:
        print("invalid choice dummy")
    
sl.makeDir("saveData")
game()