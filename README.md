# AI Voice Agent with Real-Time Metrics  
LiveKit + OpenAI + ElevenLabs + Silero VAD

---

## Overview

**AI Voice Agent** is a **real-time, low-latency voice assistant** built on **LiveKit Agents**.  
It integrates **OpenAI Whisper (STT)**, **GPT-4o-mini (LLM)**, **ElevenLabs TTS**, and **Silero VAD** to enable **streaming voice interactions** with continuous audio input and asynchronous processing.

The system is designed for **production-ready experimentation**, allowing you to monitor detailed **performance metrics** for each stage of the pipeline without blocking the conversation flow.  

**Key Real-Time Features:**
- **Streaming audio input** with voice activity detection (VAD)
- **Async processing pipeline** for STT → LLM → TTS
- **Low-latency LLM inference** using GPT-4o-mini
- **Real-time metrics collection** without delaying responses
- **LiveKit integration** for low-latency audio streaming in rooms

This architecture ensures **responsive, conversational voice interactions** suitable for AI assistants, customer support, and other real-time applications.

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
<pre>
.  
├── main.py              # Agent implementation  
├── example.env          # Environment template  
├── .env                 # Local configuration  
├── requirements.txt     # All necessary requirements 
└── README.md
</pre>
---

## Environment Configuration

## Environment Configuration

Create a `.env` file by copying the provided template:

```bash
cp example.env .env
```
Then update the values with your actual credentials.

---

## Installation

## Installation

```bash
# Clone the repository
git clone <repository_url>

# Move into project directory
cd <project_directory>

# Create virtual environment using uv
uv venv

# Activate virtual environment

# Linux / Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

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
