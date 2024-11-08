import speech_recognition as sr
import random
import json
from gtts import gTTS
from pydub import AudioSegment
import os
from constants import *
import time
from greeting import *

# Load keywords and responses from JSON file
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)
keywords_and_responses = load_data('data.json') 
keywords = keywords_and_responses["keywords"]
responses = keywords_and_responses["responses"]

def live_speech_to_text_google():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    global equalizer_active
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                text:str = recognizer.recognize_google(audio, language="hu-HU")
                if "eve" in text.lower():
                    equalizer_active = True

                    time.sleep(1)
                    #audio = recognizer.listen(source)
                    #final_text = recognizer.recognize_google(audio, language="hu-HU")
                    
                    # Process the response and reset states
                    handle_query(text)
                    equalizer_active = False
                    #update_equalizer(equalizer_active)
                #print("Recognized Speech:", text)
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                print(f"Could not request results from Google; {e}")



def text_to_speech(text, lang="hu"):
    tts = gTTS(text=text, lang=lang)
    speek_path = "/output/output.mp3"
    speek_path_fast = "/output/output_fast.mp3"
    tts.save(speek_path)
    sound = AudioSegment.from_file(speek_path)
    faster_sound = sound.speedup(playback_speed=1.15)
    faster_sound.export(speek_path_fast, format="mp3")
    #os.system("mpg321 output.mp3")  # Or use any mp3 player
    os.system(f"mpg321 {speek_path_fast} > /dev/null 2>&1")




# Function to check for keywords in the input
def check_category(input_text):
    input_text = input_text.lower()
    # Dictionary to keep track of match counts for each category
    match_counts = {category: 0 for category in keywords}
    # Count matches for each category
    for category, word_list in keywords.items():
        for word in word_list:
            if word in input_text:
                match_counts[category] += 1
    # Find the category with the highest match count
    best_category = max(match_counts, key=match_counts.get)
    if match_counts[best_category] > 0:  # If there are matches, return the category
        return best_category
    return None  # No matches found

# Function to respond based on category
def respond_from_data(category):
    if category:
        response = random.choice(responses[category])
        if callable(response):  # If it's a function, execute it (for time queries)
            return response()
        return response
    return "Sajnos nem igazán értettem, el tudnád mondani másképp?"

def handle_query(query):
    """Processes the recognized query and triggers response generation."""
    final_category = check_category(query)
    if final_category == "greetings_daytime":
        final_response = return_greeting(query)
    else:
        final_response = respond_from_data()
    text_to_speech(final_response)