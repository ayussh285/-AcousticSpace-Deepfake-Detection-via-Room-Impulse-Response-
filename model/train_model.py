from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42, stratify=y )

    model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(report)
    
    model_folder = Path("trained_models")
    model_folder.mkdir(exist_ok=True)
    model_path = model_folder / "random_forest_v1.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved at: {model_path}")

    return model , {"accuracy": accuracy, "classification_report": report}