# House Price Prediction

This project is a simple machine learning pipeline for predicting house prices based on features such as size, number of bedrooms, and age. It uses a Linear Regression model and is implemented in Python with scikit-learn.

## Project Structure

```
HousePricePrediction/
│
├── data/                # Dataset required for training/testing
├── models/              # Saved trained models
├── src/
│   ├── train.py         # Training script for the regression model
│   ├── evaluate.py      # Model evaluation script
│   └── ...              # (Other source files)
└── README.md            # Project documentation
```

## Requirements

- Python 3.8+
- pandas
- scikit-learn

Install dependencies with:

```
pip install -r requirements.txt
```

## Usage

1. **Prepare your data**
   Ensure your dataset (CSV or DataFrame) contains the following columns:
   - `size`
   - `bedrooms`
   - `age`
   - `price`

2. **Train the model**

   In your Python environment:

   ```python
   import pandas as pd
   from src.train import train_model

   data = pd.read_csv('data/your_data.csv')
   model, X_val, y_val = train_model(data)
   ```

   The trained model will be saved to `models/model.pkl`.

3. **Evaluate the model**

   ```python
   from src.evaluate import evaluate_model

   evaluate_model(model, X_val, y_val)
   ```

   This will print the Mean Squared Error and R² Score for your validation set.

## Notes

- You can extend the feature set or try different regression algorithms for better performance.
- Make sure the `models/` directory exists before training.

## License

This project is for learning purposes.
