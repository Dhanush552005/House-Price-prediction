# 🏡 House Price Prediction

This project predicts **house prices** based on various features such as area, number of bedrooms, and amenities using **XGBoost Regression**.  
It demonstrates data preprocessing, model training, and saving the model for future use.

---

## 📘 Features

- Preprocessing of categorical and numerical data  
- Binary conversion for features like `mainroad`, `guestroom`, etc.  
- Implementation of **XGBoost Regressor**  
- Model serialization using **Joblib**  
- Clean, modular, and reusable code  

---

## 📂 Dataset

The dataset used is `Housing.csv`.  
Each row represents details of a house including:
- `area`, `bedrooms`, `bathrooms`, `stories`
- `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `parking`
- `prefarea`, `furnishingstatus`
- `price` (Target variable)

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Dhanush552005/House-Price-prediction.git
cd House-Price-prediction
pip install -r requirements.txt

---

## 📊 Model Evaluation

The performance of different regression models was compared using **Mean Absolute Percentage Error (MAPE)**.

| Model              | MAPE   |
|--------------------|--------:|
| 🟩 **XGBoost**          | **0.2491** |
| 🟨 Gradient Boosting    | 0.2522 |
| 🟦 Linear Regression    | 0.2550 |
| 🟧 Random Forest        | 0.2667 |
| 🟥 Decision Tree        | 0.2896 |

### 🔹 Conclusion
Among all models tested, **XGBoost** achieved the **lowest MAPE (0.2491)**, making it the most accurate model for house price prediction.

---
