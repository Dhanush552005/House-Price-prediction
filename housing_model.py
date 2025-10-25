import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
import joblib


df = pd.read_csv('Housing.csv')

cols = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea']
df[cols] = df[cols].applymap(lambda x: 1 if x == 'Yes' else 0)

df.drop('furnishingstatus',axis=1,inplace=True)

X = df.drop('price', axis=1)
y = df['price']

xgb_model =XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=4,
    random_state=42,
    n_jobs=-1
)

xgb_model.fit(X,y)