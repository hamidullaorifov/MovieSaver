
## Prerequisites

To run this FastAPI application using Docker, you need to have the following software installed on your machine:

- Docker

If you don't have Docker installed, you can download and install it from the [official Docker website](https://www.docker.com/get-started).

## Getting Started

To run the FastAPI application on your local machine, follow these steps:

1. Clone this repository to your local machine or download the ZIP file and extract it.

```bash
git clone https://github.com/hamidullaorifov/MovieSaver.git
```

2. Open a terminal or command prompt and navigate to the project's directory.

```bash
cd MovieSaver
```

3. Build and run the Docker containers using Docker Compose.
```bash
docker-compose up --build
```
This command will build the necessary images and start the containers in detached mode.

4. Once the containers are running, you can access the FastAPI application by opening your web browser and navigating to http://localhost:8000.

