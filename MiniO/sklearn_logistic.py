import numpy as np
from sklearn.linear_model import LogisticRegression

import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5020")
    mlflow.set_experiment("exp_test")

    X = np.array([-1, -2, 2, 1, 2, 1]).reshape(-1, 1)
    y = np.array([1, 1, 0, 0, 1, 0])
    lr = LogisticRegression()
    lr.fit(X, y)
    score = lr.score(X, y)
    print("Score: %s" % score)
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(lr, "model")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)