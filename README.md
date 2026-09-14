# SWE40006 – Docker Deployment Task 4

This repository contains the source code and Docker configuration files
developed for Task 4 of SWE40006 Software Deployment and Evolution.

## Task 4.1 – Pass

Docker Desktop was installed and verified by pulling and executing the
official Docker hello-world image.

## Task 4.2 – Credit

A basic Flask web application was developed and containerized using Docker.

The Docker image was built and tested locally, pushed to Docker Hub,
and subsequently pulled and executed on a secondary AWS EC2 Docker host.

Files are available in:
`Task-4.2-Credit/`

## Task 4.3 – Distinction

A custom Flask web application was developed and containerized using Docker.

The deployment demonstrates:
- Docker container networking
- Port mapping on port 8080
- Environment variable configuration
- Public HTTP accessibility through AWS EC2

Files are available in:
`Task-4.3-Distinction/`

## Task 4.4 – High Distinction

A non-web Python data-processing application was developed and
containerized using Docker.

The application reads numerical input, processes the data, and writes
the results to persistent host-mounted storage.

The deployment demonstrates:
- Non-web container execution
- Docker bind mounts
- Persistent output storage
- Container lifecycle management
- Docker log verification

Files are available in:
`Task-4.4-HD/`
