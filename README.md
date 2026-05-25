# Industrial AI Predictive Maintenance System

AI-powered predictive maintenance framework for industrial equipment using machine learning and industrial sensor analytics.

---

## Overview

This project develops a predictive maintenance system capable of identifying machine failure risks from operational sensor data.

The system combines:
- industrial exploratory analysis
- physics-informed feature engineering
- machine learning classification
- operational risk evaluation

to simulate predictive maintenance workflows commonly used in modern manufacturing and Industry 4.0 environments.

---

## Problem Statement

Unexpected equipment failures in industrial environments can lead to:
- production downtime
- maintenance cost escalation
- operational inefficiencies
- safety risks

The objective of this project is to proactively identify machine failure conditions using historical operational sensor data and machine learning models.

---

## Dataset

### AI4I 2020 Predictive Maintenance Dataset
Source: UCI Machine Learning Repository

The dataset contains 10,000 industrial operating records with:
- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Product quality categories
- Failure indicators

Failure conditions include:
- Tool Wear Failure (TWF)
- Heat Dissipation Failure (HDF)
- Power Failure (PWF)
- Overstrain Failure (OSF)
- Random Failure (RNF)

---

## Exploratory Data Analysis

The exploratory analysis focused on understanding operational conditions associated with machine failures.

### Key Insights
- Higher tool wear strongly correlates with machine failures
- Failure regions commonly occur under high torque and low RPM operating conditions
- Machine failures exhibit nonlinear and interaction-driven behavior
- Engineered operational indicators provide stronger separation than raw sensor variables
- The dataset contains strong class imbalance, making recall-focused evaluation important

---

## Feature Engineering

Physics-informed operational indicators were engineered to better represent industrial machine behavior.

### Engineered Features
- Temperature Difference

```math
\Delta T = T_{process} - T_{air}
```

- Estimated Mechanical Power

```math
P = \tau \cdot \frac{2\pi n}{60}
```

These engineered features improve representation of:
- thermal efficiency
- mechanical loading
- operational stress conditions

---

## Machine Learning Workflow

### Preprocessing
- Ordinal encoding for product quality categories
- Train-test split with stratification
- Feature scaling for linear models
- Multicollinearity analysis

### Models Implemented
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Evaluation Metrics
Due to class imbalance, model evaluation focuses on:
- Precision
- Recall
- F1-score
- ROC-AUC

Special emphasis is placed on recall because missed machine failures are operationally costly in predictive maintenance systems.

---

## Current Findings

Initial baseline modeling indicates:
- Tree-based models outperform linear models on industrial failure prediction tasks
- Random Forest provides stronger nonlinear failure detection capability
- Engineered features improve operational interpretability
- Failure prediction benefits significantly from interaction-aware modeling

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Repository Structure

```text
industrial-ai-predictive-maintenance/
│
├── data/
├── notebooks/
├── dashboard/
├── models/
├── screenshots/
├── reports/
├── app/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Project Workflow

1. Industrial Data Understanding
2. Exploratory Data Analysis
3. Feature Engineering
4. Preprocessing & Scaling
5. Baseline Machine Learning Models
6. Performance Evaluation
7. Predictive Maintenance Insights

---

## Future Improvements

Planned extensions include:
- Hyperparameter tuning
- XGBoost implementation
- SMOTE-based imbalance handling
- Power BI industrial dashboard
- Maintenance recommendation engine
- Streamlit deployment
- Real-time monitoring simulation

---

## Author

Sahil Singh Shekhawat