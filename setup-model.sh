#!/bin/bash
# Script to pull the qwen2:0.5b model into the running Ollama container

echo "Pulling qwen2:0.5b model..."
docker exec -it ollama ollama pull qwen2:0.5b
echo "Model pulled successfully."
