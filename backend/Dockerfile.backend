# Pull base image
FROM python:3.10.4-slim-bullseye
# Set environment variables

# Set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files from the current directory into the container at /app
COPY . .

# Make port 8000 available for the app to use
EXPOSE 8000

# Start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
