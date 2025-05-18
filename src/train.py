# training data

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

def train_model(data):
    x = data[['size', 'bedrooms', 'age']]
    y = data['price']

    X_train, X_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    #save model
    with open('models/model.pkl','wb') as f:
        pickle.dump(model, f)

    return model, X_val, y_val
