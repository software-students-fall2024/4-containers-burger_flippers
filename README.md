![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

## Overview

A web application that allows users to upload audio files, processes them using a transcription model, and saves the transcriptions for easy retrieval and management.

## Badges

![Machine Learning Client](https://github.com/software-students-fall2024/4-containers-burger_flippers/actions/workflows/machine-learning-client.yml/badge.svg)

![Web-App](https://github.com/software-students-fall2024/4-containers-burger_flippers/actions/workflows/web-app.yml/badge.svg)

## Team Members
[Christopher Li](https://github.com/christopherlii)

[Julie Chen](https://github.com/Julie-Chen)

[Maddy Li](https://github.com/maddy-li)

[Aneri Shah](https://github.com/anerivs)

## Whisper API
Utilized whisper API for transcription, and required CLT ffmpeg

## How to Run the Project through Docker

1. **Clone the repository**:
    ```bash
    git clone https://github.com/software-students-fall2024/4-containers-burger_flippers.git
    ```

2. Install pipenv if you haven't already:

```bash
pip install pipenv
```
3. Go to the web_app directory, then create a virtual environment and install dependencies:

```bash
pipenv install --dev
```

4. Add in the environment variables into the machine_learning_client folder: 
    ```bash
    MONGO_URI= <insert url>
    FLASK_HOST= <insert host>
    FLASK_PORT= <insert port>
    ```
    
5. **Start and build the docker containers**
    ```bash
    docker compose up --force-recreate --build
    ```
    
6. **Go to the website**
    Enter in the local url http://127.0.0.1:3000/.

7. **Shut down the Docker containers**
    ```bash
    docker-compose down
    ```

## How to Run Unit Tests

Install required libraries:
'''
pip install flask pytest pytest-flask
'''

Run the test suite:
'''
pytest
'''

## Notes

- No secret configuration files are needed