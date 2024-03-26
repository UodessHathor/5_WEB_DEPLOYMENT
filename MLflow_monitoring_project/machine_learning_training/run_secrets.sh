docker run -it\
 -v "$(pwd):/home/app"\
 -e MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI\
 -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID\
 -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY\
 -e BACKEND_STORE_URI=$BACKEND_STORE_URI\
 -e ARTIFACT_STORE_URI=$ARTIFACT_STORE_URI\
 mlflow_trainings_getaround python train_infer_app_gradient.py