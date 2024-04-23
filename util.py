import google.generativeai as genai
from PIL import Image

# Local
from constants import INSTRUCTIONS_PROMPT


# Function to call the Gemini LLM API (you'll need to replace with actual API details)
def get_instructions(image: Image, gemini_model: genai.GenerativeModel) -> str:
    response = gemini_model.generate_content([
        INSTRUCTIONS_PROMPT,
        image,
    ])
    response.resolve()
    return response.text

