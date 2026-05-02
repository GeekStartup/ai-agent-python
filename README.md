# AI Agent Python

A simple learning project to understand how AI agents work.

## Features
- AI chat using OpenAI
- Simple math tool
- Routes user input to either:
  - TOOL for calculations
  - AI for normal questions
- Uses `.env` for API key

## Project Structure
- `main.py` - main program loop
- `ai.py` - OpenAI calls and action decision
- `tools.py` - calculator tool

## Setup
```bash
pip install openai python-dotenv