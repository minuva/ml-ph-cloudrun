# Google cloud run

gcloud auth login
gcloud config set project forecasthub

docker build --tag gcr.io/forecasthub/postlangml .
docker push gcr.io/forecasthub/postlangml

gcloud run deploy cloud-ml-app --platform managed --region europe-west3 --image gcr.io/forecasthub/postlangml --service-account app-dev@forecasthub.iam.gserviceaccount.com --allow-unauthenticated


gcloud run deploy cloud-ml-app --platform managed --region europe-west3 --image gcr.io/forecasthub/postlangml --service-account app-dev@forecasthub.iam.gserviceaccount.com --allow-unauthenticated --port 9612 --memory 4Gi


gcloud run deploy cloud-ml-app --platform managed --region europe-west3 --image gcr.io/forecasthub/postlangml --service-account app-dev@forecasthub.iam.gserviceaccount.com --allow-unauthenticated --port 9612 --memory 4Gi --set-env-vars CLOUDRUN_SERVICE_URL=https://cloud-ml-app-qnb6bcsgwa-ey.a.run.app,SECRET_KEY=$SECRET_KEY