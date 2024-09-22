Twilio Voice Call with Real-time Transcription and AI Response
This project demonstrates how to build an interactive voice call system using Twilio's Voice API, Whisper for real-time transcription, and OpenAI's LLM for generating conversational responses. The system streams live audio during a phone call, processes voice transcription in real-time, generates an AI-based response, and converts it back to speech using Text-to-Speech (TTS).

Features
Real-time Voice Streaming: Stream audio from a Twilio phone call to the backend.
Voice Activity Detection (VAD): Use WebRTC's VAD to detect when the caller is speaking.
Real-time Transcription: Whisper model transcribes speech into text.
AI Response Generation: OpenAI LLM processes the transcribed text and generates a conversational response.
Text-to-Speech (TTS): Convert the AI response into speech and play it back to the caller.
Project Structure
├── agent
│   └── client.py             # Client-side script to initiate the Twilio call
├── server
│   ├── app.py                # Flask server to handle Twilio webhooks and stream audio
│   ├── helper.py             # Helper functions for transcription, VAD, and LLM query
│   ├── requirements.txt      # Required Python packages
│   └── .env                  # Environment variables for API keys (not included in Git)
└── README.md                 # This file

