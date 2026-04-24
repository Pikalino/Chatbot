# AI Chatbot (Tool-Using Agent)

A simple AI chatbot that can execute functions and interact with local tools.

Built while following the Boot.dev AI agent course, focused on understanding how LLMs can call functions and perform tasks programmatically.

## Features

- Chat-based interaction
- Function calling (tool execution)
- File read/write operations
- Modular function system
- Basic prompt handling

## Project Structure

- `main.py` — entry point
- `call_function.py` — function execution logic
- `functions/` — available tools
- `prompts.py` — system + user prompts
- `config.py` — configuration
- `calculator/` — example tool module

## Tech Stack

- Python
- OpenAI API (or compatible LLM API)
- uv

## What I Learned

- How LLM function calling works
- Structuring an AI agent loop
- Tool abstraction and execution
- Prompt design basics
- Handling file-based operations programmatically

## Run Locally

```bash
uv run main.py
