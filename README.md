![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

## Overview

A web application that allows users to upload audio files, processes them using a transcription model, and saves the transcriptions for easy retrieval and management.

## Badges

![Machine Learning Client](https://github.com/software-students-fall2024/4-containers-burger_flippers/actions/workflows/event-logger.yml/badge.svg)

![Web-App](https://github.com/software-students-fall2024/4-containers-burger_flippers/actions/workflows/event-logger.yml/badge.svg)

## Team Members
[Christopher Li](https://github.com/christopherlii)

[Julie Chen](https://github.com/Julie-Chen)

[Maddy Li](https://github.com/maddy-li)

[Aneri Shah](https://github.com/anerivs)

## [Whisper API](https://github.com/openai/whisper)
Utilized whisper API for transcription, and required CLT ffmpeg

## How to Run the Project through Docker

To run the application, open Docker Desktop and then:
```
docker-compose build ml-client
```

## How to Run Unit Tests

Install required libraries:
```
pip install flask pytest pytest-flask
```

Run the test suite:
```
pytest
```