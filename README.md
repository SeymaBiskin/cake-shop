# Cake-Shop

## Description
This project is a web application for a cake shop with a FastAPI backend running in Docker containers managed by Docker Compose. It provides a scalable and portable way to run your cake shop application and its dependencies.

## Prerequisites
Before getting started, make sure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started
1. Clone this repository to your local machine:
   ```shell
   git clone https://github.com/SeymaBiskin/cake-shop.git
2. Navigate to the project directory:
   ```shell
   cd cake-shop
3. Build and start the Docker containers with Docker Compose:
   ```shell
   docker-compose up -d
4. The FastAPI application should now be running. You can access it in your web browser at
   ```shell
   http://localhost:8000/docs

## Project Structure
```plaintext
cake-shop/
│
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI application code
│   │   ├── models.py         # Data models
│   │   ├── routers/          # API route handlers
│   │   ├── database.py       # Business logic and services
│   │   
│   │   
│   │
│   ├── Dockerfile            # Dockerfile for the FastAPI application
│   ├── requirements.txt      # Python dependencies
│   
│
├── docker-compose.yml        # Docker Compose configuration
│
├── .env                      # File for environment variables
├── README.md                 # README file


