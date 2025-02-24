import subprocess
import threading

def run_backend():
    subprocess.run(["uvicorn", "Backend.main:app", "--host", "0.0.0.0", "--port", "10000"])

def run_frontend():
    subprocess.run(["streamlit", "run", "frontend/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"])

# Run backend in a separate thread
backend_thread = threading.Thread(target=run_backend)
backend_thread.start()

# Run frontend
run_frontend()
