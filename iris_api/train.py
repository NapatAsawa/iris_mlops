import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib  # For saving the model
from loguru import logger
import os

# Load dataset
if __name__ == '__main__':
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train XGBoost model
    clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42)
    clf.fit(X_train, y_train)

    # Save model
    os.makedirs("model", exist_ok=True)
    model_path = "model/iris_model.pkl"
    joblib.dump(clf, model_path)
    logger.info(f'saved model {model_path}')
