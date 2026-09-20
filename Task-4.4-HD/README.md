# Task 4.4 – High Distinction Level

## Non-Web Data Processing Container

### Navigate to Project
cd C:\Users\Hp\Downloads\docker-data-processor

### Verify Project Files
dir

### Build Docker Image
docker build -t docker-data-processor .

### Verify Docker Image
docker images

### Run Container with Host-Mounted Input and Output
docker run --name data-processor -v "${PWD}\input:/data/input" -v "${PWD}\output:/data/output" docker-data-processor

### Verify Container Lifecycle
docker ps -a

### Check Container Logs
docker logs data-processor

### Remove Completed Container Before Re-execution
docker rm data-processor

### Re-run Container After Modifying Input
docker run --name data-processor -v "${PWD}\input:/data/input" -v "${PWD}\output:/data/output" docker-data-processor

### Verify Re-executed Container
docker ps -a

### Check Updated Logs
docker logs data-processor
