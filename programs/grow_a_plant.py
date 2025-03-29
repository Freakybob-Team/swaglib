import swaglib as sl
import random as rd

print("grow a plant | 0.0.1")

file_path = "saveData/save.json"
default_stats = {"level": 0, "xp": 0, "required_xp": 10, "watering_can_level": 1}

playerStats = sl.loadJson(file_path) if sl.fileExists(file_path) else default_stats

def water():
    global playerStats
    
    random_xp = rd.randint(5, 10 + playerStats["level"] * playerStats["watering_can_level"])
    playerStats["xp"] += random_xp
    
    if playerStats["xp"] > playerStats["required_xp"]:
        
        playerStats["level"] += 1
        print(f'you leveled up! you are now level {playerStats["level"]}.')
        
        
        playerStats["xp"] -= playerStats["required_xp"]
        playerStats["required_xp"] += 50 
        return
        
    print(f'+{random_xp}.')
    
    
def exit_game():
    exit()
    
def wateringCanLevel():
    global playerStats
    
    required_level = playerStats["watering_can_level"] * 2
    
    if playerStats["watering_can_level"] < 5 and playerStats["level"] > required_level:
        playerStats["watering_can_level"] += 1
        print(f"Watering can upgraded! New level: {playerStats['watering_can_level']}")
        
        sl.saveJson(playerStats, "saveData/save.json")
        
    elif playerStats["level"] < required_level:
        print(f"you need to be level {required_level} in order to get the next upgrade!")
        
    else:
        print("error")
    
def shop():
    shop_options = {
        "1":wateringCanLevel
    }
    
    print("1. better watering can")
    
    option = str(input())
    
    if option in shop_options:
        shop_options[option]()
        game()
    else:
        print("invalid choice dummy")
    

def game():
    
    options = {
        "1": water,
        "2": shop,
        "3": exit_game
    }
    
    print("1. water your plant\n2. go to the shop\n3. exit")
    option = str(input())
    
    if option in options:
        options[option]()
        sl.saveJson(playerStats, "saveData/save.json")
        game()
    else:
        print("invalid choice dummy")
        game()
    
sl.makeDir("saveData")
game()