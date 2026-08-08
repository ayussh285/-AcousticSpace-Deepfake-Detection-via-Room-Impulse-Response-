from ml.create_dataset import create_dataset
from model.train_model import train_model
import numpy as np

def main():

    print("Creating dataset...")
    X, y = create_dataset()

    print("Training model...")
    print(np.bincount(y))
    model, metrics = train_model(X, y)

    print("\nAccuracy")
    print(metrics["accuracy"])

    print("\nClassification Report")
    print(metrics["classification_report"])


if __name__ == "__main__":
    main()