from ml.create_dataset import create_dataset
from model.train_model import train_model
from pathlib import Path

def main():
    dataset_path = Path("dataset")
    X, y = create_dataset(dataset_path)
    train_model(X, y)
    print(X.shape)
    print(y.shape)
    print("Training completes...")

if __name__ == "__main__":
    main()