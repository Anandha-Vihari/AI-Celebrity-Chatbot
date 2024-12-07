# 🌟 AI Celebrity Chatbot

## 📋 Project Overview
An innovative AI-powered chatbot that simulates realistic conversations with celebrities using state-of-the-art open-source large language models.

## 🎯 Project Objective
Develop an advanced conversational AI platform that enables users to interact with virtual representations of celebrities, leveraging sophisticated natural language processing and machine learning technologies.

## 📙 Features

### 🤖 Advanced AI Capabilities
- Hyper-realistic celebrity personality simulation
- Context-aware conversational intelligence
- Deep learning-powered response generation

### 🌐 Celebrity Interaction
- Diverse celebrity persona library
- Customizable interaction parameters
- Multi-domain celebrity representations (Entertainment, Sports, Politics, Science)

### 🧠 Technical Innovations
- Open-source LLM integration
- Real-time personality trait modeling
- Adaptive communication algorithms

## 🫳 Prerequisites

### Hardware Requirements
- Processor: 8+ CPU cores
- RAM: 16+ GB
- Storage: 60+ GB
- Recommended: NVIDIA CUDA-compatible GPU

### Software Requirements
- Python 3.11+
- Node.js 20.16.0+
- Flask
- SQLAlchemy
- Ollama
- Llama3/Gemma/Mistral LLMs

## 👣 Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/AI-Celebrity-Chatbot.git
cd AI-Celebrity-Chatbot
```

### 2. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
# venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### Ollama Setup

#### Installing Ollama
```bash
# Windows (WSL2 required)
curl -fsSL https://ollama.com/install.sh | sh

# Verify Installation
ollama --version
```

### Pull required models
```bash
ollama pull mistral    # Balanced performance (default)
ollama pull llama3     # Creative responses
ollama pull gemma      # Efficient processing  
ollama pull starcoder  # Technical expertise

#### Verify models are installed
ollama list
```

## 🗂 Project Structure
```
AI-Celebrity-Chatbot/
├── abilities/
│   ├── llm.py
│   ├── migrations.py
│   ├── __init__.py
├── instance/
│   └── database.db
├── migrations/
│   └── database.sql
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── chat.js
│       ├── header.js
│       └── home.js
├── templates/
│   ├── chat.html
│   ├── home.html
│   └── partials/
│       ├── _desktop_header.html
│       ├── _header.html
│       └── _mobile_header.html
├── app_init.py
├── main.py
├── models.py
├── routes.py
└── requirements.txt
```

## 🚀 Running Application
```bash
# Start development server
python main.py
```

---

**Revolutionizing Digital Interactions, One Celebrity at a Time** 🌟
