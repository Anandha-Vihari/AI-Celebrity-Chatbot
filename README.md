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

# 🚀 Deploy on Spheron

Here I will help you to deploy Server and Ollama on Spheron using Spheron Protocol CLI 💪

## Prerequisites

You should have this before you start deploying on Spheron:
- `curl`

## 1. Install Spheron Protocol CLI (Linux, MacOS)

```bash
curl -sL1 https://sphnctl.sh | bash
```

After installation, verify the installation by using a simple command to check the Spheron version:

```bash
sphnctl version # or `sphnctl -h` for help
```

## 2. Creating a Wallet

```bash
sphnctl wallet create --name <your-wallet-name>
```

Replace `<your-wallet-name>` with your desired wallet name. Here is an example of how the result will look:

```
Created account xxx:
 path: root/.spheron/<your-wallet-name>.json
 address: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 secret: xxxxxxxxxx
 mnemonic: xxxxxx xxxxx xxxx xxxxx xxxxx xxxx xxxxx xxxxx
```

**Important:** Make sure to securely save the mnemonic phrase and key secret provided.

## 3. Get Test Tokens from the Faucet

You will need some token to deploy on Spheron. Visit the Spheron Faucet to obtain test tokens for deployment. 

After receiving the tokens, you can check your wallet balance with:

```bash
sphnctl wallet balance --token USDT
```

Here is an example of how the result will look:

```
Current ETH balance: 0.00011 (used for gas fee)
Total USDT balance: 35 (used to buy the lease)
 
Deposited USDT balance
 unlocked: 100.0000
 locked: 0.0000
```

## 4. Deposit Tokens to Your Escrow Balance

Deposit USDT to your escrow wallet for deployment:

```bash
sphnctl payment deposit --amount 20 --token USDT
```

```bash
sphnctl wallet balance --token USDT
```
### 5. Create your Deployment

deploy the `deploy.yml` configuration file on Spheron:
```bash
sphnctl deployment create deploy.yml
```
Here is an example of how the result will look:
```bash
Validating SDL configuration.
SDL validated.
Sending configuration for provider matching.
Create deployment tx: [Tx Hash]
Waiting for providers to bid on the deployment order...
Bid found.
Order matched successfully.
Deployment created using wallet xxxxxxxxxxxxxxxxxxxxxxx
 lid: xxxx
 provider: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 agreed price: 0.30
Sending the manifest for deployment…
Deployment manifest sent, waiting for acknowledgment.
Deployment is finished.
```
'lid' is used access the deployment,lid also means lease id
### 6. Access Your Deployment
To get details about your deployment, including the URL, ports, and status, run:
```bash
sphnctl deployment get --lid <lease-id>
```
Replace the `<lease-id>` with your actual Lease ID, you obtained after deployment.

You will get a url that is your deployment link

## ✍ Acknowledgments
This project couldn't be there if they didn't be there!
- [Spheron](https://spheron.network/)
- [Ollama](https://ollama.com/library)
- [Llama3](https://ollama.com/library/llama3)
- [Gemma](https://ollama.com/library/gemma)
- [Mistral](https://ollama.com/library/mistral)

---

**Revolutionizing Digital Interactions, One Celebrity at a Time** 🌟
