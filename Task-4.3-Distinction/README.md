# Task 4.3 – Distinction Level

## Local Docker Deployment

### Navigate to Project
cd C:\Users\Hp\Downloads\docker-flask-distinction

### Build Docker Image
docker build -t docker-flask-distinction .

### Verify Image
docker images

### Run Container with Networking and Environment Variables
docker run -d -p 8080:8080 -e APP_ENV=Production -e APP_MESSAGE="Running with Docker environment variables" --name flask-distinction docker-flask-distinction

### Verify Running Container
docker ps

### Verify Environment Variables
docker exec flask-distinction env

### Check Container Logs
docker logs flask-distinction


## Docker Hub Deployment

### Tag Image
docker tag docker-flask-distinction bhavana105684108/docker-flask-distinction:latest

### Verify Tagged Image
docker images

### Push Image
docker push bhavana105684108/docker-flask-distinction:latest


## AWS EC2 Public Deployment

### Pull Image from Docker Hub
sudo docker pull bhavana105684108/docker-flask-distinction:latest

### Run Container with Port Mapping and Environment Variables
sudo docker run -d -p 8080:8080 -e APP_ENV=Production -e APP_MESSAGE="AWS EC2 Docker Deployment" --name flask-distinction bhavana105684108/docker-flask-distinction:latest

### Verify Running Container
sudo docker ps

### Verify Environment Variables
sudo docker exec flask-distinction env

### Check Container Logs
sudo docker logs flask-distinction
