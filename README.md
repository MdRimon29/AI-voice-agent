# AI Voice Agent with Real-Time Metrics  
LiveKit + OpenAI + ElevenLabs + Silero VAD

---

## Overview

This project implements a low-latency, real-time voice agent using a modular pipeline architecture built on top of LiveKit Agents. It integrates speech recognition, language modeling, and speech synthesis into a unified streaming system, while exposing fine-grained performance metrics across each stage.

The system is designed for production-oriented experimentation, enabling benchmarking of latency, throughput, and responsiveness across STT, LLM, and TTS components.

---

## Architecture

Audio Input  
→ Voice Activity Detection (Silero VAD)  
→ Speech-to-Text (OpenAI Whisper)  
→ LLM Inference (OpenAI GPT)  
→ Text-to-Speech (ElevenLabs)  
→ Audio Output  

Each component emits asynchronous metrics without blocking the real-time pipeline.

---

## Key Features

- Real-time voice interaction
- Streaming-first architecture
- Event-driven metrics collection
- Async execution model
- Modular and extensible design
- Pluggable models and providers

---

## Metrics & Observability

The system captures detailed runtime metrics:

### LLM Metrics
- Prompt tokens
- Completion tokens
- Tokens per second
- Time to First Token (TTFT)

### STT Metrics
- Processing duration
- Audio duration
- Streaming status

### End-of-Utterance Metrics
- Utterance detection delay
- Transcription delay

### TTS Metrics
- Time to First Byte (TTFB)
- Synthesis duration
- Audio duration
- Streaming status

---

## Tech Stack

- Python (asyncio)
- LiveKit Agents
- OpenAI (Whisper + GPT)
- ElevenLabs (TTS)
- Silero VAD

---

## Project Structure

.
├── main.py              # Agent implementation
├── example.env          # Environment template
├── .env                 # Local configuration
└── README.md

---

## Environment Configuration

Create a `.env` file:

OPENAI_API_KEY=your_openai_api_key  
ELEVEN_API_KEY=your_elevenlabs_api_key  

LIVEKIT_URL=your_livekit_url  
LIVEKIT_API_KEY=your_livekit_api_key  
LIVEKIT_API_SECRET=your_livekit_api_secret  
LIVEKIT_TOKEN=your_livekit_token  

Notes:
- Do not wrap values in quotes unless necessary
- Restart the application after updating `.env`

---

## Installation

git clone <repository_url>  
cd <project_directory>  

python -m venv venv  
source venv/bin/activate        # Linux/Mac  
venv\Scripts\activate           # Windows  

pip install -r requirements.txt  

---

## Run the Agent

python main.py dev  

This will:
- Start a LiveKit worker
- Connect to a room
- Begin real-time voice interaction
- Output metrics to the console

---

## Configuration

### Model Selection

Default:

llm = openai.LLM(model="gpt-4o-mini")

Options:
- gpt-4o → higher quality
- gpt-4o-mini → lower latency and cost

---

### Agent Behavior

instructions = "You are a helpful assistant communicating via voice"

Modify this to adapt the agent for:
- Customer support
- Voice copilots
- Domain-specific assistants

---

## Design Principles

Low Latency:
- Streaming pipeline
- Minimal blocking operations

Observability:
- Event-driven metrics
- Fine-grained latency tracking

Modularity:
- Decoupled STT / LLM / TTS components
- Easy provider replacement

---

## Common Issues

No audio output:
- Check system output device
- Validate ElevenLabs API key

Microphone not working:
- Verify input device
- Check OS permissions

Agent not responding:
- Verify LiveKit credentials
- Ensure room connection

.env not loading:
- Ensure file is saved
- Restart application

---

## Production Considerations

- Replace console logs with structured logging
- Integrate Prometheus or OpenTelemetry
- Add retry and fault tolerance for APIs
- Use secure secret management
- Containerize with Docker

---

## Future Improvements

- Streaming partial LLM responses
- Multi-agent orchestration
- Memory and context persistence
- Speaker diarization
- Edge deployment support

---

## License

MIT License
