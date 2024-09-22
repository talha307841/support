import os
import webrtcvad
import whisper
import openai
from gtts import gTTS
from dotenv import load_dotenv
import twilio
from twilio.rest import Client

# Load API keys from the environment variables
load_dotenv()

# OpenAI and Twilio setup
openai.api_key = os.getenv('OPENAI_API_KEY')
twilio_client = Client(os.getenv('TWILIO_API_KEY'), os.getenv('TWILIO_AUTH_TOKEN'))

# Initialize WebRTC VAD
vad = webrtcvad.Vad()

def is_speech(frame, sample_rate=16000):
    """Check if the given audio frame contains speech."""
    return vad.is_speech(frame, sample_rate)

# Initialize Whisper Model
model = whisper.load_model("base")

def transcribe_audio(audio_data):
    """Transcribe audio data using Whisper."""
    result = model.transcribe(audio_data)
    return result['text']

def query_llm(text):
    """Query the LLM (GPT-3 or GPT-4) for a response."""
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=text,
        max_tokens=150
    )
    return response['choices'][0]['text']

# Text-to-Speech (TTS) using gTTS
def text_to_speech(text, filename="response.mp3"):
    """Convert text to speech and save it to a file."""
    tts = gTTS(text)
    tts.save(filename)
    os.system(f"mpg321 {filename}")  # Ensure 'mpg321' is installed or use another player like ffmpeg or VLC
