from src.load_data import load_dataset
from src.train import train_model
from src.evaluate import evaluate_model

def main():
    data = load_dataset('data/dataset.csv')
    model, X_val, y_val = train_model(data)
    evaluate_model(model, X_val, y_val)

if __name__ == '__main__':
    main()
