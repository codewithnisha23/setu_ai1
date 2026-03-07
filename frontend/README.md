# SetuAI – AI Assistant for Government Schemes

## Overview

SetuAI is a multilingual AI assistant that helps citizens discover and understand government welfare schemes easily.
Users can ask questions using text or voice and receive responses in multiple Indian languages. The system also includes an eligibility calculator to quickly check qualification for welfare programs.

This project was built for the **AI Bharat Hackathon**.

---

## Key Features

### 🤖 AI Scheme Assistant

Users can ask questions about government schemes such as:

```
PM Kisan scheme
Housing scheme
Health insurance scheme
```

The AI searches a local knowledge base and provides a simple explanation.

---

### 🌐 Multilingual Support

The assistant supports multiple languages:

* English
* Hindi
* Marathi
* Tamil
* Bengali

Users can choose their preferred language from the interface.

---

### 🎤 Voice Assistant

Users can interact using voice:

* Speech-to-text input
* Text-to-speech responses

This allows accessibility for non-technical users.

---

### 📊 Eligibility Calculator

Users can enter their annual income to quickly check eligibility for government welfare programs.

---

## Architecture

```
User (Voice / Text)
        ↓
Frontend (HTML + JavaScript)
        ↓
FastAPI Backend
        ↓
AI Engine (Language Detection)
        ↓
RAG Scheme Search
        ↓
Response Generation
        ↓
Speech Output
```

---

## Technology Stack

**Frontend**

* HTML
* CSS
* JavaScript
* Web Speech API

**Backend**

* Python
* FastAPI

**AI Components**

* Language Detection (langdetect)
* RAG-style scheme search

---

## Project Structure

```
setu-ai/
│
├── main.py
├── ai_engine.py
├── rag_engine.py
├── voice.py
├── users.py
│
├── data/
│   └── schemes.json
│
└── frontend/
    └── index.html
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/setu-ai.git
cd setu-ai
```

Install dependencies:

```
pip install fastapi uvicorn langdetect
```

---

## Running the Backend

Start the FastAPI server:

```
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

## Running the Frontend

Navigate to the frontend folder:

```
cd frontend
python -m http.server 5500
```

Open the application:

```
http://localhost:5500
```

---

## Example Usage

Ask questions like:

```
PM Kisan scheme
Ayushman Bharat
Housing scheme
```

The assistant will respond with scheme details and speak the answer.
