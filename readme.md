<div align="center">

# ChatGPT Chatbot  
A simple command-line chatbot powered by OpenAI’s `gpt-3.5-turbo` model.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

</div>

---
| **Category** | **Details** |
|---------------|-------------|
| 🧠 Model | OpenAI GPT-3.5-turbo |
| 💻 Language | Python 3.7+ |
| 🔐 Auth | Environment variable or `.env` |
| ⚙️ Interface | Command-line (Terminal) |

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Security Note](#security-note)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features
- Interactive chat interface in the terminal
- Powered by OpenAI's `gpt-3.5-turbo`
- Secure API key handling (no hardcoded credentials)
- Simple and clean Python implementation

---

## Prerequisites
- **Python 3.7+**
- **OpenAI API key** (create one from the OpenAI platform)

---

## Installation

Clone this repository:
```bash
git clone https://github.com/sirrakanthikiran/my-first-ai-chatbot.git
cd my-first-ai-chatbot
```

### Install required dependencies:
```
pip install openai
```

### If you plan to use a .env file, also install:
```
pip install python-dotenv

```
## Setup

### Choose one of the methods below to provide your API key.

#### Option A — Enter key when prompted (easiest)

##### Just run the script and paste your API key when asked.

#### Option B — Set environment variable (recommended)

Windows (Command Prompt):
```
set OPENAI_API_KEY=your-key-here
python chatbot.py
```
macOS / Linux (bash):

```
export OPENAI_API_KEY=your-key-here
python chatbot.py
```
### Option C — Use a .env file (advanced)

#### 1. Copy .env.example to .env.

#### 2. Put your key inside:
```
OPENAI_API_KEY=your-key-here
```
#### 3. Ensure your script loads environment variables (e.g., with python-dotenv).

## Usage
Run the chatbot:
```
python chatbot.py
```
Type your messages and press Enter. Type quit to exit.

Example
```
You: What is Python?
Bot: Python is a high-level, interpreted programming language...

You: quit
Goodbye!
```
## Project Structure
my-first-ai-chatbot/
├── chatbot.py          # Main chatbot script
├── .gitignore          # Protects API keys and local env files
├── .env.example        # Example environment file
└── README.md           # This file

## Security Note
Never commit your actual API key to version control.
Ensure .env is listed in .gitignore.

Example .gitignore snippet:
```
.env
*.env
__pycache__/
*.pyc
```

## Troubleshooting

item Command not found: python” → Try python3 instead of python.

ModuleNotFoundError: No module named 'openai'” → Run pip install openai.

Key not found → Confirm you set OPENAI_API_KEY (environment or .env).

Windows PowerShell → Use $env:OPENAI_API_KEY="your-key-here" instead of set.

## License

MIT License — feel free to use and modify.


---
## Author
**Dr. Kanthi Kiran Sirra**  
GitHub: [@sirrakanthikiran](https://github.com/sirrakantihkiran)


---
Made with ❤️ using OpenAI’s GPT-3.5-turbo
