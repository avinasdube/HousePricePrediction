import pandas as pd
import numpy as np

np.random.seed(42)

size = np.random.randint(500, 4000, size=100)
bedrooms = np.random.randint(1, 5, size=100)
age  = np.random.randint(0, 30, size=100)


price = size * 300 + bedrooms * 5000 - age * 1000 + np.random.normal(0, 10000, size=100)

df = pd.DataFrame({
    'size': size,
    'bedrooms': bedrooms,
    'age': age,
    'price': price
})

df.to_csv('dataset.csv', index=False)
