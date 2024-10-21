
# FastAPI Machine Learning Model Deployment

This project demonstrates how to deploy a machine learning model using FastAPI. The project includes a RESTful API for making predictions from a trained model and is containerized using Docker for easy deployment.

## Features
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Docker**: Containerized environment for easy deployment and scalability.
- **Machine Learning Model**: Deployed for inference, capable of predicting results based on input data.

## Requirements
- **Docker**: Make sure Docker is installed on your machine.
- **Python** (if running locally): Python 3.9 or later.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-ml-deployment.git
cd fastapi-ml-deployment
```

### 2. Model and Preprocessor

- Place machine learning model (`model.pkl`) in the project directory.

### 3. Build the Docker Image

Build the Docker image using the provided `Dockerfile`:

```bash
docker build -t my-fastapi-app .
```

### 4. Run the Docker Container

Run the Docker container exposing it on port 8000:

```bash
docker run -d --name fastapi-container -p 8000:8000 my-fastapi-app
```

### 5. Test the API

Once the container is running, the FastAPI app will be accessible at `http://localhost:8000/docs#/default/predict_predict_post`.

- Visit `http://localhost:8000/docs#/default/predict_predict_post/` to see the root endpoint.

### 6. Making Predictions

You can use the `/predict` endpoint to get predictions from the deployed machine learning model. Below is an example of the input format:

```json
{
  "Age": 65,
  "LengthOfStay": 5,
  "AR_DRG": "B70A",
  "Principal_ProcedureCode": "03.91",
  "CareType": "Acute",
  "SourceOfReferral": "GP",
  "UrgencyOfAdmission": "Emergency",
  "AgeGroup": "60-70",
  "WeekendStay": 1,
  "Sex": "M"
}
```

Send a POST request to:

```
POST http://localhost:8000/docs#/default/predict_predict_post
```

### 7. Stopping the Docker Container

To stop and remove the running Docker container:

```bash
docker stop fastapi-container
docker rm fastapi-container
```

## Project Structure

```
.
├── main.py               # FastAPI app
├── Dockerfile            # Dockerfile to containerize the app
├── requirements.txt      # Python dependencies
├── models/.pkl             # Trained machine learning model (add this file)
└── README.md             # Project documentation
```

