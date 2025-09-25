#  Phishing URL Classifier

An end-to-end machine learning project that detects phishing websites based on 49 engineered features. This project includes data preprocessing, model training, evaluation, and deployment via both Flask and Streamlit web apps.

---

## Project Structure

PHISHING_CLASSIFIER/

src/

data/ → Data loading, preprocessing, and scaler saving

model/ → Model training, evaluation, and saving

utils/ → Utility functions (e.g., scaling, logging)

inference/ → Inference notebook (infer_model.ipynb)

templates/

index.html → HTML form for Flask app

app.py → Flask web app for prediction

streamlit_app.py → (Optional) Streamlit version of the app

requirements.txt → Python dependencies

README.md → Project documentation



---

##  Dataset

- **Source**: [Phishing_Legitimate_full.csv on Kaggle](https://www.kaggle.com/datasets/monasahoo/phishing-website)
- **Features**: 49 numerical features extracted from URLs
- **Target**: `CLASS_LABEL`  
  - `1` → Phishing  
  - `0` → Legitimate

---

##  Model Training

- Models used:
  -  Random Forest
  -  XGBoost
- Evaluation:
  - Accuracy comparison
  - Best model selected and saved as `phishing_model.pkl`
- Scaler saved for consistent inference

---

##  Inference

- Notebook: `infer_model.ipynb`
- Loads saved model and scaler
- Accepts new input (manual or CSV)
- Returns prediction: **Phishing 🚨** or **Legitimate ✅**

---

## Web App (Flask)

- File: `app.py`
- UI: `templates/index.html`
- Accepts all 49 features via form
- Displays prediction with styled result
- Includes link to Kaggle dataset for input reference

---

Setup Instructions:

git clone https://github.com/ABHINAV1111-WEB/Phishing_Classifier

Install dependencies: pip install -r requirements.txt




##  How to Run

### 1. Install dependencies
pip install -r requirements.txt


 ## Run Flask app

python app.py







