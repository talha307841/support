# Twilio Voice Call with Real-time Transcription and AI Response

This project demonstrates an interactive voice call system using Twilio's Voice API, WebRTC for real-time voice streaming, Whisper for transcription, and OpenAI's GPT-4 for generating responses. The system handles live audio during a phone call, processes transcription, queries an AI model, and responds with synthesized speech.

## Features
- **Real-time Voice Streaming**: Audio from a Twilio phone call is streamed in real-time to the backend.
- **Voice Activity Detection (VAD)**: Utilizes WebRTC's VAD to detect when the caller is speaking.
- **Real-time Transcription**: The Whisper model transcribes the caller's speech into text.
- **AI-based Response**: OpenAI's GPT-4 generates a conversational response based on the transcribed text.
- **Text-to-Speech (TTS)**: Converts the AI-generated text into speech and plays it back to the caller.

## Project Structure
- `main.py`: Handles the server setup, Twilio webhook, and communication with the client.
- `helper.py`: Contains helper functions for voice detection, transcription, AI querying, and text-to-speech conversion.
- `client.py`: Allows you to initiate a call using the Twilio API.

## Prerequisites

- **Python 3.8+**
- **Twilio Account**: [Sign up here](https://www.twilio.com/try-twilio) if you don't have one.
- **Twilio Phone Number**: You need a verified Twilio phone number.
- **OpenAI API Key**: Get your API key from [OpenAI](https://platform.openai.com/).
- **Whisper Model**: The project uses OpenAI's Whisper model for transcription.
- **LocalTunnel (or Ngrok)**: For exposing your localhost to Twilio.

### Required Python Packages
- `twilio`
- `flask`
- `whisper`
- `webrtcvad`
- `openai`
- `dotenv`
- `pyaudio`
  
Install these by running:
```bash
pip install -r requirements.txt
