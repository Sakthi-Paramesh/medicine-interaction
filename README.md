# HumanEase AI – Intelligent Medicine Interaction & Prescription Safety System

**HumanEase AI** is a premium, enterprise-grade SaaS web application built with **Spring Boot 3.4** and **Java 21**. It empowers users to search for medicines, understand complex side effects, check dangerous drug interactions using Google Gemini AI, and scan physical prescriptions via Tesseract OCR.

---

## 🚀 Key Features

*   **Intelligent Medicine Search**: Instantly look up thousands of medicines with live autocomplete functionality.
*   **AI Medicine Assistant**: Powered by Google Gemini 2.5 Flash. If a medicine isn't in the local database, the AI will dynamically generate a highly detailed and medically formatted summary.
*   **Drug Interaction Checker**: Enter multiple medicines and receive a detailed safety report (Safe, Moderate, Dangerous) regarding how the drugs interact with each other.
*   **Prescription Scanner (OCR)**: Drag & Drop a prescription image to automatically extract text using Tess4J, and feed it into the AI Interaction Checker.
*   **Premium SaaS UI**: A beautiful, modern interface featuring glassmorphism, dynamic animations, dark/light modes, and loading skeletons.
*   **Secure Authentication**: Role-based access control (Admin & User) using Spring Security and stateless JWT tokens via HTTP-Only Cookies.

---

## 🛠 Technology Stack

### Backend
*   **Java 21**
*   **Spring Boot 3.4.1**
*   **Spring Security & JWT** (Authentication)
*   **Spring Data JPA & Hibernate** (ORM)
*   **Maven** (Dependency Management)

### AI & Integrations
*   **Google Gemini API** (`RestTemplate` client)
*   **Tess4J** (Tesseract OCR Wrapper for Java)

### Frontend
*   **Thymeleaf** (Server-Side Rendering)
*   **Bootstrap 5** (Responsive Grid & Components)
*   **Vanilla JS & CSS3** (Animations, Dark Mode, API Fetching)

### Database
*   **MySQL 8** (Relational Database)

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed on your machine:

1.  **Java Development Kit (JDK) 21**
2.  **Apache Maven** (Optional if using embedded wrapper, but recommended)
3.  **MySQL Server** (Running on `localhost:3306`)
4.  **Tesseract OCR** (Must be installed on your system. For Windows, download and install it, ensuring `tessdata` is present in `C:/Program Files/Tesseract-OCR/tessdata`).

---

## 💻 Setup & Installation

### 1. Database Configuration
Create a new MySQL database named `humanease`:
```sql
CREATE DATABASE humanease;
```
The application will automatically create the required tables (`spring.jpa.hibernate.ddl-auto=update`).

### 2. Configure Properties
Open `src/main/resources/application.yml` and verify your database credentials. 
Add your **Google Gemini API Key**:
```yaml
gemini:
  api:
    key: "YOUR_GEMINI_API_KEY_HERE"
    url: "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
```

### 3. Build & Run
Open your terminal in the project root directory and run:
```bash
mvn clean install
mvn spring-boot:run
```

The application will start on **http://localhost:8080``**.

---

## 📂 Project Structure (Clean Architecture)

```
src/main/java/com/humanease/
├── config/         # App configurations
├── controller/     # REST APIs and Web View Controllers
├── dto/            # Data Transfer Objects
├── entity/         # JPA Entities (User, Medicine)
├── exception/      # Global Exception Handling
├── repository/     # Spring Data Repositories
├── security/       # JWT Filters, UserDetails, SecurityConfig
├── service/        # Business Logic (OCR, AI, Auth, Medicine)
└── util/           # Helper classes
```

---

## 🛡 Security Notes

*   **JWT Storage**: JWT tokens are securely stored in HTTP-Only Cookies to prevent XSS attacks while allowing seamless navigation across Thymeleaf pages.
*   **Passwords**: User passwords are encrypted using `BCryptPasswordEncoder`.

---

## 📜 License
This project is proprietary and built for demonstration purposes. Medical disclaimers apply: AI-generated content should not substitute professional medical advice.
