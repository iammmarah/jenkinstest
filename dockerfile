# Dockerfile

# Use a lightweight official Python image as the base.
# This ensures that Python and necessary dependencies are available.
FROM python:3.9-slim-buster

# Set the working directory inside the container.
# All subsequent commands will be executed relative to this directory.
WORKDIR /app

# Copy the requirements.txt file into the container.
# This file lists all the Python dependencies for the Flask application.
COPY requirements.txt .

# Install the Python dependencies specified in requirements.txt.
# The --no-cache-dir flag helps keep the image size down.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code (app.py) into the container.
COPY app.py .

# Expose port 5000, which is the port our Flask application listens on.
# This tells Docker that the container will listen on this port.
EXPOSE 6789

# Define the command to run when the container starts.
# This will execute the Flask application.
# The '0.0.0.0' host is crucial for the app to be accessible from outside the container.
CMD ["python", "app.py"]

