# 💊 MedSafety — Intelligent Medicine Interaction & Prescription Safety System

**MedSafety** is a full-stack web application built with **Python (Django)** that helps users search for medicines, check drug interactions, scan prescriptions via OCR, and get AI-powered medical summaries using **Google Gemini AI**.

> ⚠️ **Medical Disclaimer**: This project is built for educational and portfolio purposes only. AI-generated content should **never** substitute professional medical advice.

---

## 📸 Pages Overview

| Page | Route | Description |
|---|---|---|
| Home | `/` | Landing page |
| Register | `/register` | User registration |
| Login | `/login` | User login |
| Dashboard | `/dashboard` | Personalized user dashboard |
| Medicine Search | `/search` | Search medicines from the database |
| Medicine Detail | `/medicine/<id>` | Detailed medicine info page |
| AI Medicine Detail | `/medicine/ai` | AI-generated medicine summary |
| Drug Interaction | `/interaction` | Check interactions between multiple drugs |
| Prescription Scanner | `/scanner` | Upload & scan a prescription image via OCR |
| Saved Medicines | `/saved` | View your saved medicines |

---

## 🚀 Key Features

- **🔍 Medicine Search** — Instantly search from a database of 40+ medicines with detailed info
- **🤖 AI Medicine Assistant** — Uses Google Gemini (`gemini-1.5-flash`) to generate detailed medical summaries for medicines not in the local database
- **💊 Drug Interaction Checker** — Enter multiple medicines and get a **Safe / Moderate / Dangerous** interaction report powered by Gemini AI
- **📷 Prescription Scanner (OCR)** — Upload a prescription image; Tesseract OCR extracts the text, and Gemini AI analyzes medicine names and flags dangerous combinations
- **🔐 User Authentication** — Register, login, and logout with Django's auth system
- **🔖 Save Medicines** — Authenticated users can bookmark medicines for later reference
- **📜 Search History** — Tracks recent searches per user

---

## 🛠 Technology Stack

### Backend
| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Django 5+ | Web framework |
| SQLite3 | Database |

### AI & Integrations
| Technology | Purpose |
|---|---|
| Google Gemini AI (`gemini-1.5-flash`) | Medicine summaries, drug interaction analysis, prescription analysis |
| Tesseract OCR + `pytesseract` | Extract text from uploaded prescription images |
| Pillow | Image processing for OCR and AI vision |

### Frontend
| Technology | Purpose |
|---|---|
| Django Templates | Server-side rendering |
| Bootstrap 5 | Responsive UI components |
| Vanilla JS & CSS3 | Interactivity and custom styles |

---

## 📁 Project Structure

```
medsafety/
├── core/                        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── medsafety_app/               # Main Django app
│   ├── models.py                # Database models (User, Medicine, SavedMedicine, SearchHistory)
│   ├── urls.py                  # URL routing (web + API)
│   ├── views/
│   │   ├── web_views.py         # Renders HTML pages
│   │   └── api_views.py         # REST API endpoints (JSON)
│   └── services/
│       ├── ai_service.py        # Google Gemini AI integration
│       └── ocr_service.py       # Tesseract OCR integration
│
├── templates/                   # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── search.html
│   ├── medicine_detail.html
│   ├── medicine_ai_detail.html
│   ├── interaction.html
│   ├── scanner.html
│   ├── saved_medicines.html
│   └── user_dashboard.html
│
├── static/                      # Static assets (CSS, JS, images)
├── seed_40_medicines.py         # Seeds the DB with 40+ medicines
├── manage.py
├── requirements.txt
└── .env                         # Environment variables (NOT committed)
```

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.10+**
2. **Tesseract OCR**
   - **Windows**: Download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and install it. Then uncomment and set the path in `ocr_service.py`:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```
   - **Linux/macOS**: Install via package manager:
     ```bash
     sudo apt install tesseract-ocr      # Ubuntu/Debian
     brew install tesseract              # macOS
     ```
3. **Google Gemini API Key** — Get one free at [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 💻 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sakthi-Paramesh/medicine-interaction.git
cd medicine-interaction
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> The `.env` file is listed in `.gitignore` and will **not** be committed to version control.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed the Database

Populate the database with 40+ pre-built medicines:

```bash
python seed_40_medicines.py
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to: **http://127.0.0.1:8000/**

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/auth/register` | Register a new user |
| `POST` | `/api/auth/login` | Login |
| `POST` | `/api/auth/logout` | Logout |
| `GET` | `/api/medicines/search?q=<query>` | Search medicines |
| `GET` | `/api/medicines/<id>` | Get medicine details by ID |
| `POST` | `/api/user/save/<medicine_id>` | Save a medicine |
| `DELETE` | `/save/<medicine_id>` | Unsave a medicine |
| `GET` | `/save/status/<medicine_id>` | Check if a medicine is saved |
| `GET` | `/api/user/saved` | Get all saved medicines |
| `GET` | `/api/user/recent-searches` | Get recent search history |
| `POST` | `/api/ai/interaction` | Check drug interactions via AI |
| `POST` | `/api/medicines/scan` | Scan prescription image via OCR + AI |

---

## 🗃 Database Models

| Model | Description |
|---|---|
| `User` | Extended Django user with `role` (USER / ADMIN) |
| `Medicine` | Stores full medicine details (dosage, side effects, interactions, warnings, etc.) |
| `SavedMedicine` | Tracks which medicines a user has saved |
| `SearchHistory` | Records each user's search queries |

---

## 🛡 Security Notes

- The `.env` file is excluded from version control via `.gitignore`. **Never commit your API keys.**
- This project uses Django's built-in session-based authentication.
- All sensitive configuration (API keys) is loaded via `python-dotenv`.

---

## 📦 Dependencies

```
Django>=5.0
Pillow>=10.0.0
pytesseract>=0.3.10
google-generativeai>=0.4.0
python-dotenv>=1.0.0
```

---

## 📜 License

This project is built for **educational and portfolio purposes**. Free to use and modify.

---

## 👨‍💻 Author

**Sakthi Paramesh**
GitHub: [@Sakthi-Paramesh](https://github.com/Sakthi-Paramesh)
