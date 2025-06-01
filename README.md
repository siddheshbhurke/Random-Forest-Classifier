# Random Forest Classifier Web App

A web-based machine learning application built using **Streamlit** that classifies input data using the **Random Forest algorithm**. The model is trained on a structured dataset and deployed via **Streamlit Cloud** for easy access and interaction.

---

## 🔍 Overview

This project demonstrates a supervised classification system using the **Random Forest** algorithm, an ensemble learning method that constructs multiple decision trees and outputs the mode of their predictions.

### 🔢 What is Random Forest?

Random Forest is a powerful machine learning algorithm based on the ensemble of decision trees:
- It builds multiple decision trees during training.
- Each tree is trained on a random subset of data (bagging).
- Final prediction is made by **majority voting** (classification) or **averaging** (regression).
- It reduces overfitting and improves accuracy compared to a single decision tree.

---

## 📊 Dataset Used

- Format: CSV
- Type: Structured/tabular data
- Dataset name : 1) iris.csv
> Ensure dataset is clean, preprocessed (label encoding, missing value imputation, etc.) before training.

---

## 🧠 Model Details

- Algorithm: **RandomForestClassifier** from `scikit-learn`
- Model serialized using `joblib` for fast loading in production.

---

## 💻 Tech Stack

| Component        | Tool/Library         |
|------------------|----------------------|
| Backend ML Model | `scikit-learn`, `joblib` |
| Web Framework    | `Streamlit`          |
| Data Processing  | `pandas`, `numpy`    |
| Deployment       | `Streamlit Cloud`    |

---

## 📦 Requirements

List all packages in `requirements.txt`. Core dependencies include:

```bash
streamlit
scikit-learn
pandas
numpy
joblib
```
### Install via : 
```bash 
pip install -r requirements.txt
```
---
## 🧰 Key Features
- 📁 Load and process dataset
- 📊 Predict outcomes based on user input
- 🧠 Visualize model outputs (optional)
- 📝 Display prediction results in real time
- 🧪 Optional: show confusion matrix, accuracy, precision, recall
- 💾 Model caching for performance optimization
---
## User Interface 
- Built entirely using Streamlit
- UI Components:
  - Sidebar inputs for user-defined feature values
  - Main panel for prediction output
---
## 🌐 Live Deployment
The app is live and accessible via Streamlit Cloud:
[Click Here for Live Project](https://random-forest-classifier-iris.streamlit.app/)
---

## ✅ Future Enhancements
- Upload custom datasets for inference
- Add feature importance visualization
- Model retraining UI component
- Export prediction results as CSV
- Authentication for restricted access
--- 
## Author Details 
**Siddhesh – Artificial Intelligence & Data Science Engineering Student**
- LinkedIn : [siddheshbhurke](https://www.linkedin.com/in/siddheshbhurke/)
- Github : [siddheshbhurke](https://www.github.com/siddheshbhurke/)
