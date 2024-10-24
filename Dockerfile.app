# Use the official Python image as the base image (try the non-slim version if slim is causing issues)
FROM python:3.9

# Set environment variables to avoid buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY . /app/

# Make the bin/run_services.sh script executable
RUN chmod +x ./bin/run_services.sh

# Expose the necessary ports
EXPOSE 8001 4201

# Run services via the run_services.sh script
CMD ["bash", "bin/run_services.sh"]
