import os
#import streamlit as st

GEMINI_API_KEY = 'AIzaSyDWlRdJLFr7v9nUWmADlypMM3CkPhc1_5U'

LLM_OUTPUT_LENGTH_SIZE = 1024
LOGO_PATH = "asset/logo.png"
STREAMLIT_CLOUD_HOSTNAME = "localhost"

STREAMLIT_HOMEPAGE_CONTENT = """
<style>
.stApp {
    background-color: #E6E6FA;
}

.reportview-container .markdown-text-container {
    color: #4B0082;
}

.reportview-container .css-1d391kg {
    color: #4B0082;
}

h1, h2, h3, h4, h5, h6 {
    color: #4B0082;
    font-weight: bold;
}

.stButton>button {
    color: #FFFFFF;
    background-color: #9370DB;
}

.stFileUploader .css-1m6mopr {
    color: #FFFFFF;
    background-color: #9370DB;
}
</style>
"""

RECYCLING_INSTRUCTIONS_PROMPT = """
Based on the image from a game, generate a text describing the corresponding video game background music of this scene (no vocals). 
Determine the theme, tempo, emotion, instruments, timbre of the music based on the game genre, the atmosphere, 
and the player's mood. IMPORTANT: For the output, start with this template: a (emotion) song, with (instruments), describing (theme).  
3 sentences max.
"""

RECYCLING_LOCATIONS_PROMPT_COORDINATES = """
Based on the image give me all the locations nearby to geo-coordinates (latitude, longitude): ({}, {}).
I can sell or recycle this item. Give top three locations based on the ratings and distance from the mentioned location's city. 
Make sure to include the address, phone number, and website for each location.
Your locations should be relevant to the item in the image and should include recycling centers, donation centers, or other places where the item can be repurposed or recycled.
Please ensure that the locations are within a reasonable distance from the user's current location.
Give the output in a tabular format in markdown.
"""

RECYCLING_LOCATIONS_PROMPT_DURHAM = """
Based on the image give me all the locations nearby to Durham, NC, USA.
I can sell or recycle this item. Give top three locations based on the ratings and distance from the mentioned location's city. 
Make sure to include the address, phone number, and website for each location.
Your locations should be relevant to the item in the image and should include recycling centers, donation centers, or other places where the item can be repurposed or recycled.
Please ensure that the locations are within a reasonable distance from the given location.
Give the output in a tabular format in markdown.
"""