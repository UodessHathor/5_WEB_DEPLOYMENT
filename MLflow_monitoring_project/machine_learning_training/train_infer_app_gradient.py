# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
#                                  M O D E L    T R A C K I N G    W I T H     M L  F L O W         
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

# DOYON-DOUSSE Doriane (ds-fs-od-03) *****************************************************************************************


# ----------------------------------------------------------------------------------------------------------------------------
# Librairy importations °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

import mlflow
import time 
import numpy as np
import argparse
import pandas as pd
import matplotlib.pyplot as plt 
from mlflow.models.signature import infer_signature


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import LinearSVR, SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, accuracy_score
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ----------------------------------------------------------------------------------------------------------------------------
# Tracking code (ML Flow) °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

if __name__ == "__main__":
    
    EXPERIMENT_NAME = "GETAROUND-PROJECT-pricing-deployment" # Set variables for environment
    mlflow.set_tracking_uri("https://doshdyndss-mlflow-getaround-30ede0bed4eb.herokuapp.com/") # Set your tracking uri
    mlflow.set_experiment(EXPERIMENT_NAME) # Set experiment's info
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME) # Get our experiment info

    client = mlflow.tracking.MlflowClient()
    run = client.create_run(experiment.experiment_id)

    start_time = time.time()

    mlflow.sklearn.autolog(log_models=False)

    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators")
    parser.add_argument("--min_samples_split")
    args = parser.parse_args()


# USING A GRADIENT BOOSTING REGRESSOR MODEL 
    print("-------------------------------------------------------------------------------------------------------------")
    print("--------------------     P R E P R O C E S S I N G    &    M O D E L   P I P E L I N E   --------------------")
    print("-------------------------------------------------------------------------------------------------------------")

    mlflow.sklearn.autolog() # Call mlflow autolog

    pricing_df = pd.read_csv('https://jedha-deployment.s3.amazonaws.com/get_around_pricing_project.csv', index_col=0) # charge dataframe


    # Seperate label from features (X and Y) - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('Seperating target from features : - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    target = 'rental_price_per_day'
    Y = pricing_df.loc[:, target]
    X = pricing_df.drop(target, axis=1)
    print('X variables : ')
    print(X.head(10))
    print()
    print('Y target variable : ')
    print(Y.head(10))
    print()
    print('...Done! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    print()

    # Splitting into Train & Test sets  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('Splitting into train set and test set ... - - - - - - - - - - - - - - - - - - - - - ')
    print()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=23)
    print('...Done! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    print()


    # Pipeline  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('Creating pipeline for numerical & categorical features & preprocessor - - - - - - - ')
    print()
    numerical_features = [1, 2]
    numerical_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])

    categorical_features = [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    categorical_transformer = Pipeline(steps=[
        ('encoder', OneHotEncoder(drop='first', handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)])
    print('...Done! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    print()

    # Preprocessing X  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('Creating pipeline for numerical & categorical features & preprocessor - - - - - - - ')
    print()
    print('- - - - - Preprocessing is in progress on the training set  - - - - - ')
    print()
    print('X_train before preprocessing : ')
    print()
    print(X_train.head())
    print()
    print('X_train after preprocessing : ')
    print()
    X_train = preprocessor.fit_transform(X_train)
    print(X_train[0:5, :])
    print()
    print(' ===================================================================================================== ')    
    print()
    print('- - - - - - - Preprocessing is in progress on the test set - - - - - -')
    print()
    print('X_test before preprocessing : ')
    print()
    print(X_test.head())
    print()
    print('X_test after preprocessing : ')
    print()
    X_test = preprocessor.transform(X_test)
    print(X_test[0:5, :])

    print('Pipeline & Preprocessing ----> Done ! °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
    print()
    print()
    
    print("-------------------------------------------------------------------------------------------------------------")
    print("--------------------------     M O D E L   T R A I N I N G   &    S C O R E S     ---------------------------")
    print("-------------------------------------------------------------------------------------------------------------")
    print()
    print()

    # Model - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('Instanciate model, parameters & grid search - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    
    n_estimators = int(args.n_estimators)
    min_samples_split=int(args.min_samples_split)

    model = Pipeline(steps=[
        ('Preprocessing', preprocessor),
        ("Regressor",RandomForestRegressor(n_estimators=n_estimators, min_samples_split=min_samples_split))
    ])

    print('...Done! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    print()


    # Model - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('Model train & scores... - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()

    with mlflow.start_run(run_id = run.info.run_id) as run:
        model.fit(X_train, Y_train)
        predictions = model.predict(X_train)

        # Log model seperately to have more flexibility on setup 
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="GETAROUND_infer_tracking",
            registered_model_name="GETAROUND_random_forest_regressor",
            signature=infer_signature(X_train, predictions)
        )
    
    print('...Done! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print()
    print()
        
    print(f"---Total training time: {time.time()-start_time}")

    print('Model training & Performances ----> Done ! °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
    print()
    print("----------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------")


# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
#                                            E  N  D      O  F      S  C  R  I  P  T        
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------