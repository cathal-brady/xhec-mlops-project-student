#!/bin/bash

# Start Prefect server on port 4201
echo "Starting Prefect server..."
prefect server start --host 0.0.0.0 --port 4201 &

# Start FastAPI application on port 8001
echo "Starting FastAPI server..."
uvicorn src.web_service.main:app --host 0.0.0.0 --port 8001 &

# Wait for both services to finish
wait
