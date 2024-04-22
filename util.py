import google.generativeai as genai
from PIL import Image

# Local
from constants import RECYCLING_INSTRUCTIONS_PROMPT, RECYCLING_LOCATIONS_PROMPT_COORDINATES, RECYCLING_LOCATIONS_PROMPT_DURHAM, STREAMLIT_CLOUD_HOSTNAME


#__current_system_hostname__ = socket.gethostname()


# Function to call the Gemini LLM API (you'll need to replace with actual API details)
def get_recycling_instructions(image: Image, gemini_model: genai.GenerativeModel) -> str:
    response = gemini_model.generate_content([
        RECYCLING_INSTRUCTIONS_PROMPT,
        image,
    ])
    response.resolve()
    return response.text

