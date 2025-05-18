# This module provides a function to evaluate regression models using MSE and R^2 metrics.

from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_val, y_val):
    y_pred = model.predict(X_val)
    mse = mean_squared_error(y_val, y_pred)
    r2 = r2_score(y_val, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")
