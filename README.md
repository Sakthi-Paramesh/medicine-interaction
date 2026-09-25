# Intelligent Medicine Interaction & Prescription Safety System

**Intelligent Medicine Safety** is a modern web application built with **Python (Django)**. It empowers users to search for medicines, understand complex side effects, check dangerous drug interactions using Google Gemini AI, and scan physical prescriptions via Tesseract OCR.

---

## 🚀 Key Features

*   **Intelligent Medicine Search**: Instantly look up detailed information on various medicines.
*   **AI Medicine Assistant**: Powered by Google Gemini. If a medicine isn't fully detailed in the local database, the AI will dynamically generate a highly detailed and medically formatted summary.
*   **Drug Interaction Checker**: Enter multiple medicines and receive a detailed safety report (Safe, Moderate, Dangerous) regarding how the drugs interact with each other.
*   **Prescription Scanner (OCR)**: Upload a prescription image to automatically extract text using Tesseract OCR, and feed it into the AI Interaction Checker.
*   **Clean Portfolio UI**: A clean, professional, medical-themed interface built with Bootstrap 5 and custom CSS.

---

## 🛠 Technology Stack

### Backend
*   **Python 3**
*   **Django 5+** (Web Framework)
*   **SQLite3** (Database)

### AI & Integrations
*   **Google Gemini AI API** (`google-genai` / `google-generativeai`)
*   **Tesseract OCR** (`pytesseract` for Python)

### Frontend
*   **Django Templates** (Server-Side Rendering)
*   **Bootstrap 5** (Responsive Grid & Components)
*   **Vanilla JS & CSS3** (Interactive elements)

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed on your machine:

1.  **Python 3.10+**
2.  **Tesseract OCR**:
    *   **Windows**: Download and install from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki). Ensure the installation path is added to your environment variables or correctly referenced in `ocr_service.py`.
    *   **Linux/Mac**: Install via your package manager (e.g., `sudo apt install tesseract-ocr`).

---

## 💻 Setup & Installationss

### 1. Clone & Environment Setup
Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/Sakthi-Paramesh/medicine-interaction.git
cd medicine-interaction
python -m venv venv

# Activate Virtual Environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Database Setup & Seeding
Run migrations and populate the database with initial medicine data:
```bash
python manage.py makemigrations
python manage.py migrate

# Seed the database with 40+ default medicines
python seed_40_medicines.py
```

### 5. Run the Server
Start the Django development server:
```bash
python manage.py runserver
```
The application will start on **http://127.0.0.1:8000/**.

---

## 🛡 Security Notes

*   **API Keys**: The `.env` file containing secrets is added to `.gitignore` and must never be pushed to public repositories.
*   **Medical Disclaimer**: This project is built for demonstration and portfolio purposes. AI-generated content should not substitute professional medical advice.

---

## 📜 License
This project is built for educational and portfolio purposes.
