# **Retriever Bot**

**Table of Contents**

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Set Up Environment Variables](#4-set-up-environment-variables)
- [Usage](#usage)
  - [Running the Application Locally](#running-the-application-locally)
  - [Exposing the Application to Dialogflow](#exposing-the-application-to-dialogflow)
  - [Running the Scraping Script](#running-the-scraping-script)
- [Dockerization](#dockerization)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
  - [Using Docker Compose](#using-docker-compose)
- [Continuous Integration and Deployment](#continuous-integration-and-deployment)
  - [Docker Build and Push Workflow](#docker-build-and-push-workflow)
- [Scheduling Scraping ](#scheduling-scraping)
  - [Scheduled Scraping Workflow](#scheduled-scraping-workflow)
  - [Workflow Steps](#workflow-steps)
- [Environment Variables](#environment-variables)
- [Acknowledgements](#acknowledgements)
- [Additional Notes](#additional-notes)
  - [Setting Up Dialogflow](#setting-up-dialogflow)
  - [Deployment](#deployment)
  - [Security Considerations](#security-considerations)
  - [Logging ](#logging-and-monitoring)

---

## Overview

This project is a conversational AI chatbot designed to assist students with information related to courses, research, and general queries. It integrates with Dialogflow for intent recognition and uses OpenAI's GPT-3.5-turbo model for generating responses. The application leverages LangChain for conversational retrieval and Chroma for vector storage of embeddings.

## Features

- **Intent Handling**: Custom intent mapping and management using Dialogflow.
- **Conversational Retrieval**: Retrieves relevant information based on user queries.
- **Feedback Mechanism**: Collects user feedback to improve responses over time.
- **Meta Data Filtering and Contextual Understanding**: Filters relevant metadata and provides accurate responses using memory for enhanced contextual understanding.
- **Automated Data Scraping**: Periodically scrapes and updates data embeddings.
- **Dockerized Deployment**: Containerized application for consistent and scalable deployment.
- **Continuous Integration and Deployment**: Automated builds and deployments using GitHub Actions.


## Architecture

![Architecture Diagram](architecture.png)

*Note: Include an architecture diagram showing how different components interact within your system.*

## Repository Structure

```
RetrieverBot/
├── .github/
│   └── workflows/
│       ├── docker-build.yml
├── assets/
│   └── architecture_diagram.png
├── data/
│   └── ...  # Data files used by the application
├── embeddings.py
├── feedback.py
├── intent_handler.py
├── main.py
├── prompts.py
├── query_handler.py
├── scraping.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .dockerignore
├── .gitignore
├── .env.example
```

- **.github/workflows/**: Contains GitHub Actions workflows for CI/CD.
- **assets/**: Images and assets used in documentation.
- **data/**: Directory for data files and embeddings.
- **embeddings.py**: Manages embedding models and vector stores.
- **feedback.py**: Handles user feedback mechanisms.
- **intent_handler.py**: Manages intent mapping and handling.
- **main.py**: The main application file.
- **prompts.py**: Stores prompt templates for different intents.
- **query_handler.py**: Processes queries and handles retrieval.
- **scraping.py**: Handles data scraping and preprocessing.
- **Dockerfile**: Docker configuration for containerizing the app.
- **requirements.txt**: Python dependencies.
- **.env.example**: Example environment variables file.
- **LICENSE**: License information.

## Prerequisites

- **Python 3.13**
- **Docker**
- **Git**
- **An OpenAI API Key**
- **A Dialogflow Agent**

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-project.git
cd your-project
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example environment file and fill in your credentials.

```bash
cp .env.example .env
```

Fill in `.env` with your OpenAI API key and other necessary variables.

```env
OPENAI_API_KEY=your_openai_api_key
ngrok_authentication= your_ngrok_auth
```

## Usage

### Running the Application Locally

```bash
python main.py
```

The application will start and listen on `http://0.0.0.0:5000`.

### Exposing the Application to Dialogflow

To connect Dialogflow to your local application during development, you can use `ngrok`.

```bash
ngrok http 5000
```

Copy the HTTPS URL provided by ngrok and set it as your webhook URL in Dialogflow.

### Running the Scraping Script

```bash
python scraping.py
```

This script will scrape data and update embeddings which can be scheduled for updated information.

## Dockerization

### Building the Docker Image

```bash
docker build -t your_dockerhub_username/your_repository_name:latest .
```

### Running the Docker Container

```bash
docker run -d -p 5000:5000 --env-file .env your_dockerhub_username/your_repository_name:latest
```

### Using Docker Compose

Optionally, you can use Docker Compose for more complex setups.

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - '5000:5000'
    env_file:
      - .env
```

Run:

```bash
docker-compose up -d
```

## Continuous Integration and Deployment

The project uses GitHub Actions to automate the build and deployment process.

### Docker Build and Push Workflow

Located at `.github/workflows/docker-build.yml`, this workflow triggers on every push to the `main` branch.

### Workflow Steps

- Checks out the repository.
- Sets up Python.
- Installs dependencies.
- Runs `scraping.py`.
- Commits and pushes any changes.
- Triggers the Docker build and push workflow if data has changed.

## Environment Variables

All sensitive information and configuration options are managed via environment variables.

## Acknowledgements

- [OpenAI](https://www.openai.com) for the GPT-3.5-turbo model.
- [LangChain](https://langchain.readthedocs.io/en/latest/) for conversational AI components.
- [Dialogflow](https://cloud.google.com/dialogflow) for intent handling.
- [Chroma](https://www.trychroma.com/) for vector storage.
- [GitHub Actions](https://github.com/features/actions) for CI/CD pipelines.

---

## Additional Notes

### Setting Up Dialogflow

- **Create an Agent**: Set up a Dialogflow agent in your Google Cloud project.
- **Configure Intents**: Define intents and ensure they match the ones handled in your application.
- **Set Webhook URL**: In the Dialogflow console, set the webhook URL to your application's public endpoint.

### Deployment

For production deployment, consider using a cloud provider:

- **Heroku**
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure App Service**

### Security Considerations

- **API Keys**: Never commit API keys or secrets to version control.
- **HTTPS**: Use HTTPS for all communications, especially when exposing webhooks.
- **Authentication**: Implement authentication for your endpoints if necessary.

### Logging and Monitoring

.
