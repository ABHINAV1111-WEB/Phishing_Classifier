from sklearn.preprocessing import StandardScaler
from src.config.config import SCALER_TYPE

def get_scaler():
    if SCALER_TYPE == "StandardScaler":
        return StandardScaler()
    else:
        raise ValueError(f"Unsupported scaler type: {SCALER_TYPE}")

def scale_features(X, scaler=None):
    if scaler is None:
        scaler = get_scaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = scaler.transform(X)
    return X_scaled, scaler

import joblib
import os

def save_object(obj, filename):
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(obj, f"artifacts/{filename}.pkl")



