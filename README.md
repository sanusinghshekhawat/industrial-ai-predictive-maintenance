# Industrial AI Predictive Maintenance System

AI-powered predictive maintenance system for industrial equipment using machine learning and industrial sensor analytics.

---

## Project Objective

Develop a predictive maintenance framework capable of identifying machine failure risks using operational sensor data and engineered industrial indicators.

The project focuses on:
- Machine failure prediction
- Industrial sensor analysis
- Operational risk monitoring
- Maintenance intelligence
- Physics-informed feature engineering

---

## Dataset

AI4I 2020 Predictive Maintenance Dataset  
Source: UCI Machine Learning Repository

The dataset contains industrial operating parameters including:
- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Failure modes

---

## Exploratory Data Analysis Highlights

Key findings from EDA:
- Higher tool wear strongly correlates with machine failures
- Failures commonly occur under high torque and low RPM conditions
- Engineered features such as temperature difference and estimated power provide better operational insights than raw variables
- Failure behavior appears interaction-driven rather than dependent on a single variable

---

## Feature Engineering

Created industrially meaningful features:
- Temperature Difference
- Estimated Mechanical Power

These features improve representation of:
- Thermal efficiency
- Mechanical load conditions

---

## Tech Stack

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn

---

## Project Structure

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

## Project Status

### Day 1 Completed
- Dataset understanding
- Industrial EDA
- Failure analysis
- Feature engineering
- Modeling preparation