docker run -it\
 -p 4000:80\
 -e PORT=80\
 -e AWS_ACCESS_KEY_ID=$secret1\
 -e AWS_SECRET_ACCESS_KEY=$secret2\
 -e BACKEND_STORE_URI=$secret3\
 -e ARTIFACT_STORE_URI=$secret4\
 getaround_mlflow 
