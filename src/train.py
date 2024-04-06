# train.py

import pandas as pd
from src.models import YourModelClass
from src.config import Config

def train_model():
    # Load data
    data = pd.read_csv('input/ratings.csv')

    # Preprocess data if needed

    # Initialize model
    model = YourModelClass()

    # Train model
    model.train(data)

    # Save model
    model.save_model(Config.MODEL_PATH)

if __name__ == "__main__":
    train_model()
