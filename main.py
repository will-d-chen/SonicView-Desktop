import time
import pyautogui

def take_screenshot():
    # Get the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot with the timestamp as the filename
    screenshot.save(f"screenshot_{timestamp}.png")
    
    return(f"screenshot_{timestamp}.png")

# Run the screenshot capture every 2 minutes


import os
#import streamlit as st
import google.generativeai as genai
import webbrowser
from PIL import Image
#from streamlit.components.v1 import html

import requests
import time

SUNO_API_URL = 'https://suno-api-one-tau.vercel.app/api'
SUNO_API_KEY = '-'

# Local
from constants import *
from util import *

# def open_page(url):
#     open_script= """
#         <script type="text/javascript">
#             window.open('%s', '_blank').focus();
#         </script>
#     """ % (url)
#     html(open_script)
    
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

# def main1():
#     gemini_model = __get_gemini_client__()

#     # Streamlit app interface customization
#     st.markdown(
#         STREAMLIT_HOMEPAGE_CONTENT,
#         unsafe_allow_html=True
#     )


#     st.title('SonicView')
#     st.header('Generate Background Music from in Game Images')
#     st.write('Bridging the Sensory Gap Between Sight and Sound')

#     uploaded_image = st.file_uploader(
#         "",
#         type=["png", "jpg", "jpeg"],
#     )

#     if uploaded_image is not None:
#         # Display a progress bar
#         image = Image.open(uploaded_image)
#         user_uploaded_image = image.copy()
#         file_ext = str(uploaded_image.name.split(".")[-1]).lower().strip()
#         print(file_ext)

#         # Get image size in MB using os.stat
#         image = image.resize((image.width // 2, image.height // 2))
#         # Redice image quality
#         compressed_image_name = f"temp.{file_ext}"

#         image.save(
#             compressed_image_name,
#             "JPEG" if file_ext == "jpg" else file_ext.upper(),
#             quality=25,
#             optimize=True,
#             progressive=True
#         )
#         image = Image.open(compressed_image_name)
        
#         # Print image size
#         image_size = os.stat(compressed_image_name).st_size / (1024 * 1024)
#         print(f"Compressed image size: {image_size} MB")

#         if image_size > 3.9:
#             st.error("Please upload an image less than 15MB.")
#             return
        
#         st.image(user_uploaded_image, caption='Your Uploaded Image', use_column_width=True)

#         # Get recycling instructions
#         instructions = get_recycling_instructions(image, gemini_model)
#         prompt = instructions[:200]
        
#         song_id = generate_song(prompt)
#         if instructions:
#             st.subheader("Prompt Generated:")
#             st.markdown(instructions, unsafe_allow_html=True)

#             if song_id:
                
#                 # Wait for a few seconds to allow time for the song to be generated
#                 placeholder = st.empty()

#                 # Write some text using st.write()
#                 placeholder.write("generating music...")
                
#                 # Sleep for 3 seconds
#                 time.sleep(20)
                
#                 # Replace the content of the placeholder with an empty string
#                 placeholder.write("")
                
#                 song_info = get_song_info(song_id)
    
#                 if song_info:
#                     st.subheader("Song Link:")
#                     st.markdown(song_info['audio_url'], unsafe_allow_html=True)
#                     open_page(song_info['audio_url'])
                
#                 else:
#                     st.write('Failed to retrieve song information.')
#             else:
#                 st.write('Failed to initiate song generation.')


#         else:
#             st.error("Could not get instructions for recycling this item.")

#         # Delete compressed_image_name file
#         os.remove(compressed_image_name)
    





first = 0
gemini_model = __get_gemini_client__()
while True:
    if first ==0 :
        time.sleep(5)
        first = 1
        
    
    print(take_screenshot())
    image = Image.open(take_screenshot())
    instructions = get_recycling_instructions(image, gemini_model)
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
