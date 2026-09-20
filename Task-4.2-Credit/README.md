# Task 4.2 – Credit Level

## Local Docker Deployment

### Navigate to Project
cd C:\Users\Hp\Downloads\docker-flask-app
dir

### Build Docker Image
docker build -t docker-flask-app .
docker images

### Run Container
docker run -d -p 5000:5000 --name flask-app docker-flask-app

### Verify Container
docker ps
docker logs flask-app

## Docker Hub Deployment

### Login
docker login

### Tag Image
docker tag docker-flask-app bhavana105684108/docker-flask-app:latest
docker images

### Push Image
docker push bhavana105684108/docker-flask-app:latest

## Secondary Host Deployment – AWS EC2 Ubuntu

### Update Packages
sudo apt update

### Install Docker
sudo apt install docker.io -y

### Start and Enable Docker
sudo systemctl start docker
sudo systemctl enable docker

### Verify Docker
sudo docker --version

### Pull Image from Docker Hub
sudo docker pull bhavana105684108/docker-flask-app:latest

### Verify Image
sudo docker images

### Run Container
sudo docker run -d -p 5000:5000 --name flask-app bhavana105684108/docker-flask-app:latest

### Verify Container
sudo docker ps

### Check Application Logs
sudo docker logs flask-app
