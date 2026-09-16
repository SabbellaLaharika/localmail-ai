import os
import imaplib
import smtplib
import urllib.request
import json
from dotenv import load_dotenv

# Load environment variables from .env file into os.environ
load_dotenv()

IMAP_HOST = os.environ.get("IMAP_HOST", "imap.gmail.com")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
USER = os.environ.get("IMAP_USER") or os.environ.get("SMTP_USER")
PASS = os.environ.get("IMAP_PASSWORD") or os.environ.get("SMTP_PASSWORD")

if not USER or not PASS:
    print("WARNING: IMAP/SMTP credentials are not set in environment or .env file!")



print("--- Starting Verification ---")

# 1. Test IMAP
if USER and PASS:
    try:
        print(f"Testing IMAP connection to {IMAP_HOST}:993...")
        mail = imaplib.IMAP4_SSL(IMAP_HOST, 993)
        mail.login(USER, PASS)
        print("IMAP Login Successful!")
        mail.logout()
    except Exception as e:
        print(f"IMAP Failed: {e}")
else:
    print("Skipping IMAP test: IMAP_USER / IMAP_PASS not configured in .env")

# 2. Test SMTP
if USER and PASS:
    try:
        print(f"Testing SMTP connection to {SMTP_HOST}:587 (STARTTLS)...")
        server = smtplib.SMTP(SMTP_HOST, 587)
        server.starttls()
        server.login(USER, PASS)
        print("SMTP Login Successful!")
        server.quit()
    except Exception as e:
        print(f"SMTP Failed: {e}")
else:
    print("Skipping SMTP test: SMTP_USER / SMTP_PASS not configured in .env")

# 3. Test Ollama
try:
    print("Testing local Ollama model (llama3:8b)...")
    url = 'http://localhost:11434/api/generate'
    data = json.dumps({"model": "llama3:8b", "prompt": "Say hi!", "stream": False}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode('utf-8'))
        print("Ollama Responded: " + result.get("response", "").strip())
except Exception as e:
    print(f"Ollama Failed: {e}")

print("--- Verification Complete ---")
