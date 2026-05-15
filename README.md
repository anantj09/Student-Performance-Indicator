---
title: Student Performance Predictor
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
license: mit
---


# 🎓 PredictSP: Student Performance Predictor

An end-to-end machine learning web application that predicts a student's **Math score** based on demographic and academic background features. Built with a modular ML pipeline and served via a Flask web application.

---

## Problem Statement

Student academic performance is influenced by a range of socioeconomic and demographic factors. This project explores those relationships using a publicly available dataset and builds a regression model to predict math scores — helping educators and institutions identify students who may need additional support.

---

## Live Demo

> Deployed on Hugging Face Spaces — [[HFSpace Link]](https://huggingface.co/spaces/anantj09/Student-Performance-Predictor)

---

## Dataset

- **Source**: Public dataset — Students Performance in Exams
- **Size**: ~1,000 records
- **Target variable**: `math_score`
- **Features used for prediction**:

| Feature | Type | Description |
|---|---|---|
| gender | Categorical | Male / Female |
| race_ethnicity | Categorical | Group A through E |
| parental_level_of_education | Categorical | Highest education level of parent |
| lunch | Categorical | Standard or Free/Reduced |
| test_preparation_course | Categorical | Completed or None |
| reading_score | Numerical | Score out of 100 |
| writing_score | Numerical | Score out of 100 |

---

## 🧠 ML Pipeline

The project follows a clean, modular pipeline architecture:

```
data/stud.csv
     │
     ▼
DataIngestion          → splits into train.csv / test.csv → artifacts/
     │
     ▼
DataTransformation     → numerical: median imputation + StandardScaler
                       → categorical: mode imputation + OneHotEncoder + StandardScaler
                       → saves preprocessor.pkl → artifacts/
     │
     ▼
ModelTrainer           → trains 8 models with GridSearchCV hyperparameter tuning
                       → selects best by R² score
                       → saves model.pkl → artifacts/
     │
     ▼
PredictPipeline        → loads model.pkl + preprocessor.pkl
                       → transforms input → returns prediction
     │
     ▼
Flask App              → serves prediction via web form
```

---

## 🏆 Model Selection & Results

Eight regression models were trained and evaluated with 3-fold cross-validated GridSearchCV hyperparameter tuning:

| Model | Notes |
|---|---|
| Linear Regression | ✅ Best model |
| Random Forest Regressor | Hyperparameter tuned |
| Decision Tree Regressor | Hyperparameter tuned |
| Gradient Boosting Regressor | Hyperparameter tuned |
| XGBoost Regressor | Hyperparameter tuned |
| CatBoost Regressor | Hyperparameter tuned |
| AdaBoost Regressor | Hyperparameter tuned |
| K-Neighbors Regressor | — |

**Winner: Linear Regression**

> R² Score on test set: **0.8768** (~87.7% variance explained)

Linear Regression outperformed all boosting models. This is consistent with the nature of the dataset — reading and writing scores have a near-linear relationship with math scores, and with only ~1,000 rows, complex ensemble models tended to overfit rather than generalize.

---

## 🗂️ Project Structure

```
├── application.py                  # Flask app entry point
├── Dockerfile                      # Container definition
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── artifacts/
│   ├── model.pkl                   # Trained Linear Regression model
│   ├── preprocessor.pkl            # Fitted ColumnTransformer
│   ├── train.csv                   # Training split
│   └── test.csv                    # Test split
├── data/
│   └── stud.csv                    # Raw dataset
├── src/
│   ├── exception.py                # Custom exception with traceback detail
│   ├── logger.py                   # Timestamped file logging
│   ├── utils.py                    # save_object, load_object, evaluate_models
│   ├── components/
│   │   ├── data_ingestion.py       # Reads CSV, splits data
│   │   ├── data_transformation.py  # Preprocessing pipeline
│   │   └── model_trainer.py        # Training + hyperparameter tuning
│   └── pipeline/
│       └── predict_pipeline.py     # Inference pipeline + CustomData class
├── templates/
│   ├── index.html                  # Landing page
│   └── home.html                   # Prediction form + result
├── static/
│   └── style.css                   # Custom styling
└── notebook/                       # not included (the initial work)
    ├── EDA STUDENT PERFORMANCE.ipynb
    └── MODEL TRAINING.ipynb
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10.19 |
| Web Framework | Flask |
| ML Libraries | scikit-learn, XGBoost, CatBoost |
| Data Processing | pandas, numpy |
| Serialization | dill |
| Containerization | Docker |
| Deployment | Hugging Face Spaces |

---

## 🚀 Running Locally

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/student-performance-indicator.git
cd student-performance-indicator
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Flask app**
```bash
python application.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

**Using Docker**
```bash
docker build -t student-performance .
docker run -p 5000:5000 student-performance
```

---

## 🔮 How It Works

1. User visits `/predictdata` and fills in the form
2. Form data is captured by the `CustomData` class and converted to a pandas DataFrame
3. `PredictPipeline` loads the saved preprocessor and model from `artifacts/`
4. Input is transformed using the fitted preprocessor — the exact same pipeline used during training
5. The model returns a predicted math score, which is displayed on the page

---

## 👤 Author

**Anant Jain**
- Email: ja.jainanant@gmail.com
- GitHub: anantj09

---

## 📄 License

This project uses a publicly available dataset. The code is open source — feel free to fork and build on it.
