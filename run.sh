docker build -t flask_app .
docker run -d --name my_flask_app -p 50000:80 flask_app:latest
