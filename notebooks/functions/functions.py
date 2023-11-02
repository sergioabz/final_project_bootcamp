
import pandas as pd
import numpy as np

def create_dataframe_errors(y_true, y_pred):
    """"
    This function inputs the arrays, ensures that y_true and y_pred have the same length, Calculates the error, Creates a dictionary, and Creates a pandas DataFrame from the dictionary.
    """
    # Ensure that y_true and y_pred have the same length
    assert len(y_true) == len(y_pred), "Length of y_true and y_pred must be the same"

    # Calculate the error
    error = [abs(true - pred) for true, pred in zip(y_true, y_pred)]

    # Create a dictionary
    data = {
        "Real Values": y_true,
        "Predicted Values": y_pred,
        "Error": error
    }

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data)

    return df

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

def calculate_error_metrics(y_real_train, y_real_test, y_pred_train, y_pred_test)-> pd.DataFrame:
    """
    This function inputs the arrays: y_real_train, y_real_test, y_pred_train, y_pred_test and then calculates the error metrics mae, mse, rmse, r2 for the train and test set and returns a data frame.

    """
    mae_train = mean_absolute_error(y_real_train, y_pred_train)
    mse_train = mean_squared_error(y_real_train, y_pred_train)
    rmse_train = np.sqrt(mse_train)
    r2_train = r2_score(y_real_train, y_pred_train)

    mae_test = mean_absolute_error(y_real_test, y_pred_test)
    mse_test = mean_squared_error(y_real_test, y_pred_test)
    rmse_test = np.sqrt(mse_test)
    r2_test = r2_score(y_real_test, y_pred_test)

    error_metrics_df = pd.DataFrame({
        'Metric': ['MAE', 'MSE', 'RMSE', 'R2'],
        'Train': [mae_train, mse_train, rmse_train, r2_train],
        'Test': [mae_test, mse_test, rmse_test, r2_test]
    })

    return error_metrics_df


def train_models(models: list, X_train, y_train)-> list:
    trained_models = []
    for model in models:
        model.fit(X_train, y_train)
        trained_models.append(model)
    return trained_models
