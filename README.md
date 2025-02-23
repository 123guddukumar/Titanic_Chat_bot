# 🚢 Titanic Dataset Chatbot

A chatbot that answers questions about the Titanic dataset using **FastAPI** (backend) and **Streamlit** (frontend).  
It leverages **LangChain** for natural language understanding and **Matplotlib/Seaborn** for data visualization.

---

## 📂 Folder Structure

📁 Titanic-Chatbot │── 📁 backend # FastAPI Backend
│ ├── main.py # API server
│ ├── query_engine.py # Handles queries
│ ├── requirements.txt # Backend dependencies
│── 📁 frontend # Streamlit Frontend
│ ├── app.py # UI for chatbot
│ ├── requirements.txt # Frontend dependencies
│── titanic.csv # Titanic dataset
│── README.md # Project Documentation

## Features
✅ Natural Language Query Processing  
✅ Text-Based Responses  
✅ Interactive Visualizations  

## How to Run
### 1. Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### 2. Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py