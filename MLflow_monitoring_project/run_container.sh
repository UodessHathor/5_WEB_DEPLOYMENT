docker run -it\
 -p 4000:80\
 -e PORT=80\
 -e AWS_ACCESS_KEY_ID=AKIA4RMAHJJV7MKIYOEI\
 -e AWS_SECRET_ACCESS_KEY=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\
 -e BACKEND_STORE_URI=nothing\
 -e ARTIFACT_STORE_URI=s3://doshdyndss-getaround-bucket/mlflow-artefacts/\
 getaround_mlflow 


export DOCKER_DEFAULT_PLATFORM=linux/amd64