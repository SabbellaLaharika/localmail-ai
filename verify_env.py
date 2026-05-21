import imaplib
import smtplib
import urllib.request
import json

IMAP_HOST = "imap.gmail.com"
SMTP_HOST = "smtp.gmail.com"
USER = "slaharisvrsslsmr712@gmail.com"
PASS = "yvib kvzi vzll mwqi"

print("--- Starting Verification ---")

# 1. Test IMAP
try:
    print(f"Testing IMAP connection to {IMAP_HOST}:993...")
    mail = imaplib.IMAP4_SSL(IMAP_HOST, 993)
    mail.login(USER, PASS)
    print("IMAP Login Successful!")
    mail.logout()
except Exception as e:
    print(f"IMAP Failed: {e}")

# 2. Test SMTP
try:
    print(f"Testing SMTP connection to {SMTP_HOST}:587 (STARTTLS)...")
    server = smtplib.SMTP(SMTP_HOST, 587)
    server.starttls()
    server.login(USER, PASS)
    print("SMTP Login Successful!")
    server.quit()
except Exception as e:
    print(f"SMTP Failed: {e}")

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
