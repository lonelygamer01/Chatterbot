from datetime import datetime
import random
# Function to get the correct greeting based on the time of day
def get_greeting():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 10:
        return "reggelt"
    elif 10 <= current_hour <= 18:
        return "napot"
    elif 18 < current_hour <= 24 or 0 <= current_hour < 6:
        return "estét"
    
# Function to check and correct the user's greeting
def return_greeting(user_input):
    correct_daytime = get_greeting().lower()
    user_input = user_input.lower().strip().split()

    #check for morning, day, and evening greeting
    for day_indexer in user_input:
        if day_indexer in ["reggelt", "napot", "estét"]:
            daytime = day_indexer
            #if i greet her correctly
            if daytime == correct_daytime:
                return random.choice(["Önnek is uram!", f"Önnek is {random.choice(['kellemes', 'jó'])} {daytime} uram!"])
            return f"Önnek is {random.choice(['kellemes', 'jó'])} {daytime} uram! Habár {random.choice(['momentán', 'most', 'jelenleg'])} {datetime.now().hour} óra {datetime.now().minute} perc a pontos idő."

    #if no match than it must be good night
    return f"Önnek is jó {random.choice(['éjt', 'éjszakát'])} uram!"

