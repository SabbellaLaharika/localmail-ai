# Local AI Email Auto-Responder

A fully local, privacy-first AI email auto-responder built with n8n and Ollama. This system runs an LLM on your own hardware, ensuring zero data leakage to third-party providers. It checks for new emails via IMAP, prevents auto-reply loops, generates context-aware replies using `llama3:8b`, and sends responses via SMTP while maintaining the original email conversation thread.

## Features
- **100% Local Inference**: Powered by Ollama (`llama3:8b`) ensuring complete privacy.
- **Workflow Automation**: Orchestrated entirely via n8n.
- **Smart Loop Prevention**: Logic to avoid replying to the bot's own emails.
- **Dynamic Threading**: Replies use `In-Reply-To` and `References` mapping to keep conversations threaded.

## Prerequisites
- Docker and Docker Compose installed.
- Access to an email account with IMAP/SMTP credentials.

## Setup Instructions

### 1. Environment Variables Configuration
To get started, you must provide your email credentials and configuration variables. We have provided an example file.

### 1. Environment Configuration

1. Copy `.env.example` to `.env`.
2. Fill in your IMAP and SMTP credentials (see [Credentials Setup](#credentials-setup)).

### 2. Deployment

Bring up the n8n and Ollama services using Docker Compose:

```bash
docker-compose up -d
```

### 3. AI Model Initialization

Once the containers are running, you need to pull the `llama3:8b` model into the Ollama container (chosen as a small, suitable model per project requirements to fit inside memory limits). You can run the provided setup script:

```bash
chmod +x setup-model.sh
./setup-model.sh
```

*(Alternatively, run the command manually: `docker exec -it ollama ollama pull llama3:8b`)*

### 4. Import the n8n Workflow
1. Navigate to your n8n interface at [http://localhost:5678](http://localhost:5678).
2. Create a new, blank workflow.
3. Click the **Options (three dots)** menu in the top right corner and select **Import from File**.
4. Upload the `workflow.json` file found in the root of this repository.
5. In the imported workflow, open the `EmailReadImap` and `Send Email` nodes to select/setup your IMAP and SMTP credentials (you can reference the environment variables you defined in your `.env`).
6. Activate the workflow by toggling the switch in the top right corner!

## Architecture Details
1. **n8n Container**: Connects to your custom network and orchestrates the event logic.
2. **Ollama Container**: Exposes a local API on `http://ollama:11434/api/generate` that is called by n8n.
3. **Loop Prevention Node**: Halts execution if an email contains "Re: AI Auto-Reply:" to prevent an endless bot-to-bot loop.

Enjoy your private, local email assistant!
