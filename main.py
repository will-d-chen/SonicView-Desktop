import time
import pyautogui
import os
import google.generativeai as genai
import webbrowser
from PIL import Image
import requests
import time

SUNO_API_URL = 'https://suno-api-one-tau.vercel.app/api'
SUNO_API_KEY = '-'

# Local
from constants import *
from util import *

def take_screenshot():
    # Get the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot with the timestamp as the filename
    screenshot.save(f"screenshot_{timestamp}.png")
    
    return(f"screenshot_{timestamp}.png")

def __get_gemini_client__() -> genai.GenerativeModel:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-pro-vision")
    return gemini_model
def generate_song(prompt):
    url = f'{SUNO_API_URL}/generate'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SUNO_API_KEY}'
    }
    data = {
        'prompt': prompt,
        'make_instrumental': True,
        'wait_audio': False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result[0]['id']
    except requests.exceptions.RequestException as e:
        print('Error generating song:', e)
        return None

def get_song_info(song_id):
    url = f'{SUNO_API_URL}/get?ids={song_id}'
    headers = {
        'Authorization': f'Bearer {SUNO_API_KEY}'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result[0]
    except requests.exceptions.RequestException as e:
        print('Error getting song information:', e)
        return None


first = 0
gemini_model = __get_gemini_client__()
while True:
    if first ==0 :
        time.sleep(5)
        first = 1
        
    
    print(take_screenshot())
    image = Image.open(take_screenshot())
    instructions = get_instructions(image, gemini_model)
    prompt = instructions[:200]
    print(instructions)

    song_id = generate_song(prompt)

    if instructions:
        

        if song_id:
            
            # Wait for a few seconds to allow time for the song to be generated
            
            
            # Sleep for 3 seconds
            time.sleep(20)

            
            song_info = get_song_info(song_id)

            if song_info:
                print("Song Link:")
                print(song_info['audio_url'])
                webbrowser.open(song_info['audio_url'])
            
            else:
                print('Failed to retrieve song information.')
        else:
            print('Failed to initiate song generation.')


    else:
        print("Could not get instructions")

    time.sleep(90)  # Wait for roughly 2 minutes (~30 seconds needed to generate)
