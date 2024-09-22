import asyncio
import websockets
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from helper import is_speech, transcribe_audio, query_llm, text_to_speech
import threading

app = Flask(__name__)

# Twilio Webhook Route
@app.route("/twilio-webhook", methods=['POST'])
def twilio_webhook():
    """Twilio Webhook for starting the Media Stream"""
    response = VoiceResponse()
    response.start().stream(url="wss://https://twenty-snakes-write.loca.lt/audio")
    return str(response)

# WebSocket Server
async def audio_stream_handler(websocket, path):
    """Handle incoming audio stream via WebSocket from Twilio."""
    buffer = b""
    while True:
        # Receive audio frame
        frame = await websocket.recv()

        # VAD: Check if the frame contains speech
        if is_speech(frame, sample_rate=16000):
            buffer += frame

        # Once speech is done (pause), process the buffered audio
        if not is_speech(frame, sample_rate=16000) and buffer:
            # Transcribe audio using Whisper
            text = transcribe_audio(buffer)
            print(f"Transcribed Text: {text}")

            # Query LLM for response
            response_text = query_llm(text)
            print(f"LLM Response: {response_text}")

            # Convert LLM response to speech (TTS)
            tts_filename = "response.mp3"
            text_to_speech(response_text, tts_filename)

            # Play the TTS response (e.g., via WebSocket back to Twilio)
            # You will need to handle this streaming back to Twilio

            buffer = b""  # Clear buffer after processing

# Function to run Flask app
def run_flask_app():
    """Run the Flask app in a separate thread."""
    app.run(port=5000)

# Function to run WebSocket server
async def run_websocket_server():
    """Start the WebSocket server to receive audio from Twilio."""
    start_server = websockets.serve(audio_stream_handler, "localhost", 8765)
    await start_server

# Main entry point
if __name__ == "__main__":
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Run WebSocket server in asyncio event loop
    asyncio.run(run_websocket_server())
