# 🧬 MediScan — AI Disease Classifier

A machine-learning-powered disease classifier with a sleek dark-theme UI.
Analyzes your symptoms and predicts likely conditions using a Random Forest model.

---

## 🚀 Quick Start

### Option A — Auto-run (recommended)
```bash
python run.py
```
This auto-installs all missing packages and starts the server.

### Option B — Manual setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train model (only needed once)
python train_model.py

# 3. Start server
python app.py
```

Then open your browser at: **http://localhost:5000**

---

## 📦 Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for Google Fonts only; app works offline otherwise)

**Python packages** (auto-installed by run.py):
- `flask` — Web framework
- `scikit-learn` — Random Forest classifier
- `numpy` — Numerical computing
- `scipy` — Scientific computing
- `joblib` — Model serialization

---

## 🏗️ Project Structure
```
disease_classifier/
├── app.py              # Flask backend (API + routes)
├── run.py              # Smart launcher (auto-installs deps)
├── train_model.py      # Model training script
├── requirements.txt    # Python dependencies
├── models/
│   ├── classifier.pkl  # Trained Random Forest model
│   ├── symptoms.json   # List of all symptoms (90+)
│   └── disease_info.json  # Disease metadata
├── templates/
│   └── index.html      # Frontend UI
└── README.md
```

---

## 🩺 Features
- **25 diseases** classified: Flu, COVID-19, Dengue, Malaria, Diabetes, and 20 more
- **90+ symptoms** to choose from with live search
- **Top 3 predictions** with probability scores
- **Severity indicators**: Emergency / High / Chronic / Moderate / Mild
- **Matched symptoms** shown for each prediction
- **Action recommendations** for each disease
- **Disease database browser** with severity filter

---

## ⚠️ Disclaimer
This tool is for **educational and informational purposes only**.
Always consult a qualified healthcare professional for medical advice.
