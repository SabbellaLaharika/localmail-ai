#!/bin/bash
# Script to pull the llama3:8b model into the running Ollama container

echo "Pulling llama3:8b model..."
docker exec -it ollama ollama pull llama3:8b
echo "Model pulled successfully."
