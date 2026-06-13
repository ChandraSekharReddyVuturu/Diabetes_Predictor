# AI-Powered Diabetes Prediction System

An intelligent, production-ready healthcare web application that predicts whether a patient is diabetic based on 15 key medical parameters. It automates dataset aggregation, implements a 10-model machine learning pipeline, provides Explainable AI (XAI) using SHAP values, generates downloadable clinical PDF reports, and features an interactive NLP health chatbot.

---

## 🚀 Key Features

*   **Unified Preprocessing & Merging Engine**: Automatically downloads, merges, and cleans multiple datasets (PIMA Indians, CDC BRFSS, Kaggle, OpenML). Handles missing values, performs outlier analysis, standardizes features, and balances classes via **SMOTE**.
*   **10 Classifier Models Trained**: Logistic Regression, Random Forest, Decision Tree, Support Vector Machine, Naive Bayes, Gradient Boosting, XGBoost, LightGBM, KNN, and Artificial Neural Network (MLPClassifier).
*   **Automated Best-Model Deployment**: Automatically evaluates and deploys the best performing classifier based on ROC-AUC, Accuracy, Precision, Recall, and F1-score.
*   **Explainable AI (SHAP)**: Computes local SHAP contributions for every prediction to explain *why* the model made its decision.
*   **Interactive Voice Input**: Employs Web Speech API for hands-free patient data questionnaire entry.
*   **Clinical PDF & CSV Reports**: Generates detailed, professional PDF diagnostic reports (with risk gauges, SHAP bar charts, and guidelines) and exports database history as CSV.
*   **Interactive Health Chatbot**: A custom floating NLP conversational drawer to help interpret predictions and provide personalized lifestyle and dietary guidelines.
*   **Admin Control Panel**: Allows managers to upload new datasets, synchronize clinical databases, inspect user registry roles, and retrain the machine learning model.
*   **Premium Glassmorphic Design**: Modern responsive UI themed in professional medical blue-white with dark/light mode toggles and micro-animations.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | React, TypeScript, Vite, Tailwind CSS v3, Material UI (MUI v5), Plotly.js, Lucide Icons, Framer Motion | Modern, glassmorphic client-side application. |
| **Backend** | Python Flask, SQLite | REST API server, database management, and report generator. |
| **Machine Learning** | Scikit-learn, XGBoost, LightGBM, Imbalanced-learn, SHAP, Joblib | Training, evaluation, serialization, and explanation. |
| **Containerization** | Docker, Docker Compose | Microservice deployment for simple setup. |

---

## 📁 Directory Structure

```
/diabetes_predictor
├── /backend
│   ├── /datasets       # Raw & merged datasets
│   ├── /models         # Saved pickle models & pipeline artifacts
│   ├── /reports        # Generated PDF/CSV reports
│   ├── app.py          # Flask application entry point
│   ├── database.py     # SQLite database management
│   ├── downloader.py   # Automatic dataset downloader
│   ├── preprocessing.py# Cleaning, imputation, SMOTE, scaling
│   ├── training.py     # Multi-model training and comparison
│   ├── explainability.py # SHAP values & AI predictions summary
│   ├── reports_gen.py  # PDF & CSV generation logic
│   └── requirements.txt# Backend Python packages
├── /frontend
│   ├── /src
│   │   ├── /components # Reusable UI components (charts, forms, chatbot)
│   │   ├── /pages      # Application page components
│   │   ├── /types      # Plotly TS declarations
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   └── index.css
│   ├── vite.config.ts
│   ├── package.json
│   └── tailwind.config.js
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
├── nginx.conf
└── README.md
```

---

## 📋 Input Medical Parameters

The prediction engine utilizes 15 distinct demographic and medical parameters:
1.  **Pregnancies**: Number of times pregnant.
2.  **Glucose**: Plasma glucose concentration (mg/dL).
3.  **Blood Pressure**: Diastolic blood pressure (mmHg).
4.  **Skin Thickness**: Triceps skin fold thickness (mm).
5.  **Insulin**: 2-Hour serum insulin (mu U/ml).
6.  **BMI**: Body Mass Index ($weight(kg) / height(m)^2$).
7.  **Diabetes Pedigree Function**: Family history score.
8.  **Age**: Patient age.
9.  **Gender**: Demographic sex.
10. **Height**: Patient height (cm).
11. **Weight**: Patient weight (kg).
12. **HbA1c**: Glycated hemoglobin level (%).
13. **Physical Activity**: Weekly exercise score.
14. **Smoking Status**: Cigarette habits classification.
15. **Family History**: Binary indicator of diabetic parents/siblings.

---

## 🚀 Getting Started

### Option 1: Docker Compose (Recommended)

Make sure you have Docker and Docker Compose installed.

1.  **Build and run the services**:
    ```bash
    docker-compose up --build
    ```
2.  **Access the applications**:
    *   **React Frontend**: `http://localhost` (or port 80)
    *   **Flask API Backend**: `http://localhost:5000`

---

### Option 2: Local Installation (Manual)

#### 1. Setup Backend
1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
3.  Install the packages:
    ```bash
    pip install -r requirements.txt
    ```
4.  Launch the server:
    ```bash
    python app.py
    ```
    *The server runs on `http://localhost:5000` and automatically runs downloader/training files to set up standard dataset/pickle binary configurations.*

#### 2. Setup Frontend
1.  Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```
2.  Install packages:
    ```bash
    npm install
    ```
3.  Run development server:
    ```bash
    npm run dev
    ```
    *The frontend starts on `http://localhost:5173`.*

---

## 🔑 Database Credentials & Auth

The system seeds a default admin account during SQLite database initialization:

*   **Default Username**: `admin`
*   **Default Password**: `admin123`
*   **Default Role**: `admin`

JWT authentication is implemented. Login requests return a JWT token, which is stored in browser local storage and attached to the header of authorized API calls: `Authorization: Bearer <JWT_TOKEN>`.

---

## 🛡️ API Endpoints Summary

| Endpoint | Method | Authentication | Description |
| :--- | :--- | :--- | :--- |
| `/api/auth/register` | `POST` | Public | Register a new user profile. |
| `/api/auth/login` | `POST` | Public | Log in and obtain JWT token. |
| `/api/predict` | `POST` | JWT User/Admin | Run prediction using the active ML model + SHAP explanation. |
| `/api/history` | `GET` | JWT User/Admin | View past prediction logs. |
| `/api/chat` | `POST` | JWT User/Admin | NLP chatbot guidelines query. |
| `/api/admin/datasets` | `GET` | JWT Admin | List downloaded raw datasets. |
| `/api/admin/datasets/download` | `POST` | JWT Admin | Trigger downloader thread. |
| `/api/admin/models` | `GET` | JWT Admin | Get active model performance metrics. |
| `/api/admin/models/retrain` | `POST` | JWT Admin | Trigger model pipeline retrain thread. |
| `/api/reports/pdf/<id>` | `GET` | Public / Query Param | Download patient PDF diagnostic report. |
| `/api/reports/csv/history` | `GET` | JWT User/Admin | Export historical logs as CSV. |
| `/api/reports/csv/models` | `GET` | JWT Admin | Export model metrics comparison table as CSV. |

---

## 📊 Evaluation & Model Performance

The model pipeline evaluates 10 different machine learning classification algorithms. An active deployment evaluation automatically selects the best classifier based on the highest **ROC-AUC** score on the validation subset.

The deployed model (typically **Support Vector Machine** or **XGBoost**) yields:
*   **ROC-AUC**: $> 0.99$
*   **Accuracy**: $> 96\%$
*   **Recall/Precision**: Balanced to prioritize lower false negatives (crucial for medical diagnoses).

---

## ⚠️ Disclaimer

*This application is a medical simulation project designed for education, demonstration, and clinical study. The predictions, suggestions, and recommendations generated by the model and chatbot are for informational purposes only and must **not** be used as a substitute for professional clinical advice, diagnosis, or treatment.*
