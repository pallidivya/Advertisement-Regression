# Advertising Sales Prediction using Machine Learning

This project is a simple Machine Learning Regression application that predicts product sales based on advertising budgets spent on:

- TV
- Radio
- Newspaper

The project is built using:

- Python
- Scikit-learn
- Streamlit

---

# Project Overview

The model uses **Linear Regression** to predict sales from advertising data.

The workflow includes:

1. Loading the dataset
2. Data preprocessing
3. Feature scaling using `StandardScaler`
4. Train-test splitting
5. Training a Linear Regression model
6. Evaluating model performance
7. Saving the trained model
8. Deploying the model with Streamlit UI

---

# Project Structure

```bash
Advertisement-Regression/
│
├── Advertising.csv
├── train.py
├── app.py
├── advertising_model.pkl
├── requirements.txt
└── README.md
