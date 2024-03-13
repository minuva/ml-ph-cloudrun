# Google cloud run

gcloud auth login
gcloud config set project forecasthub

docker build --tag gcr.io/forecasthub/ml-ph-cloudrun .
docker push gcr.io/forecasthub/ml-ph-cloudrun

gcloud run deploy ml-ph-cloudrun-app --platform managed --region europe-west3 --image gcr.io/forecasthub/ml-ph-cloudrun --service-account app-dev@forecasthub.iam.gserviceaccount.com --port 9612 --allow-unauthenticated


gcloud run deploy ml-ph-cloudrun-app --platform managed --region europe-west3 --image gcr.io/forecasthub/ml-ph-cloudrun --service-account app-dev@forecasthub.iam.gserviceaccount.com --allow-unauthenticated --port 9612 --memory 4Gi


gcloud run deploy ml-ph-cloudrun-app --platform managed --region europe-west3 --image gcr.io/forecasthub/ml-ph-cloudrun --service-account app-dev@forecasthub.iam.gserviceaccount.com --allow-unauthenticated --port 9612 --memory 4Gi --set-env-vars CLOUDRUN_SERVICE_URL=https://ml-ph-cloudrun-app-qnb6bcsgwa-ey.a.run.app