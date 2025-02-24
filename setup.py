import subprocess
import time
import requests
import os

# Function to check if the FastAPI server is running
def is_backend_running():
    try:
        response = requests.get("http://127.0.0.1:8000/docs")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Step 1: Install Dependencies
print("📦 Installing dependencies...")
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

# Step 2: Start the FastAPI Backend
print("🚀 Starting FastAPI backend...")
backend_process = subprocess.Popen(["uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"])

# Step 3: Wait for the backend to be ready
print("⏳ Waiting for backend to start...")
for _ in range(20):  # Wait up to 20 seconds
    if is_backend_running():
        print("✅ Backend is running!")
        break
    time.sleep(1)
else:
    print("❌ Backend failed to start. Exiting...")
    backend_process.terminate()
    exit(1)

# Step 4: Start Streamlit Frontend
print("🎨 Starting Streamlit frontend...")
subprocess.run(["streamlit", "run", "frontend/app.py"], check=True)

# Step 5: Cleanup backend process on exit
backend_process.terminate()
